import tkinter as tk
from tkinter import scrolledtext, messagebox
import os
import sys
import threading
import pandas as pd

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from predict import predict_text
from train_ml import train_models


class AIDetectorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AI vs İnsan Metin Dedektörü")
        self.root.geometry("800x600")
        
        # Title
        title = tk.Label(root, text="AI vs İnsan Metin Dedektörü", font=("Arial", 16, "bold"))
        title.pack(pady=10)
        
        # Text input frame
        input_frame = tk.Frame(root)
        input_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        
        input_label = tk.Label(input_frame, text="Metni Buraya Yapıştırın:", font=("Arial", 10, "bold"))
        input_label.pack(anchor="w")
        
        self.text_input = scrolledtext.ScrolledText(input_frame, height=10, font=("Arial", 10))
        self.text_input.pack(fill=tk.BOTH, expand=True)
        
        # Button frame
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)
        
        predict_btn = tk.Button(button_frame, text="Tahmin Yap", font=("Arial", 12, "bold"), 
                               bg="green", fg="white", command=self.predict)
        predict_btn.pack(padx=5, side=tk.LEFT)
        
        teach_btn = tk.Button(button_frame, text="Öğret", font=("Arial", 12, "bold"), 
                      bg="#0066cc", fg="white", command=self.teach)
        teach_btn.pack(padx=5, side=tk.LEFT)
        
        clear_btn = tk.Button(button_frame, text="Temizle", font=("Arial", 12, "bold"), 
                             bg="orange", fg="white", command=self.clear)
        clear_btn.pack(padx=5, side=tk.LEFT)

        # Status label
        self.status_var = tk.StringVar(value="Hazır")
        status_lbl = tk.Label(root, textvariable=self.status_var, font=("Arial", 9), fg='#333')
        status_lbl.pack(pady=4)
        
        # Results frame (will hold per-model sections)
        results_frame = tk.Frame(root)
        results_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        results_label = tk.Label(results_frame, text="Sonuçlar:", font=("Arial", 10, "bold"))
        results_label.pack(anchor="w")

        # Container where per-model results widgets will be added
        self.results_container = tk.Frame(results_frame)
        self.results_container.pack(fill=tk.BOTH, expand=True)
    
    def predict(self):
        text = self.text_input.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("Uyarı", "Lütfen metin girin!")
            return
        
        try:
            results = {}
            models = ['lr', 'rf', 'svm']
            
            for model in models:
                try:
                    result = predict_text(text, model_name=model, models_dir='models')
                    results[model] = result
                except Exception as e:
                    results[model] = {'error': str(e)}
            # Clear previous result widgets
            for child in self.results_container.winfo_children():
                child.destroy()

            model_names = {
                'lr': 'Lojistik Regresyon (LR)',
                'rf': 'Rastgele Orman (RF)',
                'svm': 'Destek Vektör Makinesi (SVM)'
            }

            for model_key in models:
                frame = tk.Frame(self.results_container, bd=1, relief=tk.GROOVE, padx=8, pady=8)
                frame.pack(fill=tk.X, pady=6)

                title = tk.Label(frame, text=model_names.get(model_key, model_key), font=("Arial", 11, "bold"))
                title.pack(anchor='w')

                if 'error' in results[model_key]:
                    err_lbl = tk.Label(frame, text=f"Hata: {results[model_key]['error']}", fg='red')
                    err_lbl.pack(anchor='w')
                    continue

                result = results[model_key]
                label = result['label']
                proba = float(result['proba'])

                # Compute AI probability as ai_prob (0..1) and human_prob
                ai_prob = proba if label == 1 else (1 - proba)
                human_prob = 1 - ai_prob

                # Bar area
                bar_width = 600
                bar_height = 28
                canvas = tk.Canvas(frame, width=bar_width, height=bar_height, highlightthickness=0)
                canvas.pack(pady=6)

                # Background border
                canvas.create_rectangle(0, 0, bar_width, bar_height, outline='#555', width=1)

                fill_width = int(ai_prob * bar_width)
                color = self._prob_to_hex(ai_prob)
                if fill_width > 0:
                    canvas.create_rectangle(0, 0, fill_width, bar_height, outline='', fill=color)

                # Percent labels
                percent_text = f"AI: {ai_prob*100:.2f}%    İnsan: {human_prob*100:.2f}%"
                pct_lbl = tk.Label(frame, text=percent_text, font=("Arial", 10))
                pct_lbl.pack(anchor='w')
            
        except Exception as e:
            messagebox.showerror("Hata", f"Tahmin yapılırken hata oluştu:\n{str(e)}")

    def teach(self):
        text = self.text_input.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("Uyarı", "Lütfen metin girin!")
            return

        # modal to choose label
        modal = tk.Toplevel(self.root)
        modal.title("Etiket Seç")
        modal.geometry("320x140")
        modal.transient(self.root)
        modal.grab_set()

        lbl = tk.Label(modal, text="Bu metni kim yazdı?", font=("Arial", 11, "bold"))
        lbl.pack(pady=10)

        btn_frame = tk.Frame(modal)
        btn_frame.pack(pady=8)

        def choose_human():
            modal.destroy()
            self._label_and_train(text, 0)

        def choose_ai():
            modal.destroy()
            self._label_and_train(text, 1)

        human_btn = tk.Button(btn_frame, text="İnsan", bg="#2e8b57", fg='white', width=10, command=choose_human)
        human_btn.pack(side=tk.LEFT, padx=8)

        ai_btn = tk.Button(btn_frame, text="Makine", bg="#b22222", fg='white', width=10, command=choose_ai)
        ai_btn.pack(side=tk.LEFT, padx=8)

    def _label_and_train(self, text: str, label: int):
        """Append labeled sample to processed dataset and retrain models in background."""
        try:
            # compute processed dataset path relative to project root (gui.py sits at project root)
            root_dir = os.path.dirname(__file__)
            processed_dir = os.path.join(root_dir, 'data', 'processed')
            os.makedirs(processed_dir, exist_ok=True)
            processed_abs = os.path.join(processed_dir, 'dataset.csv')

            new_row = {'text': text.replace('\n', ' ').strip(), 'label': int(label)}
            if os.path.exists(processed_abs):
                try:
                    df = pd.read_csv(processed_abs)
                    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
                except Exception:
                    # if read fails, create new df
                    df = pd.DataFrame([new_row])
            else:
                df = pd.DataFrame([new_row])

            df.to_csv(processed_abs, index=False)
            self.status_var.set('Öğretiliyor... (model güncelleniyor)')

            # disable buttons while training
            for w in self.root.winfo_children():
                w_state = getattr(w, 'config', None)

            # run training in background thread
            t = threading.Thread(target=self._retrain_background, args=(processed_abs,))
            t.daemon = True
            t.start()
        except Exception as e:
            messagebox.showerror('Hata', f'Etiketleme sırasında hata: {e}')

    def _retrain_background(self, processed_abs):
        try:
            # call train_models (it reads processed dataset path relative to src)
            # train_models expects path relative to project root, so pass 'data/processed/dataset.csv'
            train_models(processed_path='data/processed/dataset.csv', out_dir='models')
            self.root.after(100, lambda: self.status_var.set('Eğitim tamamlandı.'))
            self.root.after(100, lambda: messagebox.showinfo('Bitti', 'Model güncellemesi tamamlandı.'))
        except Exception as e:
            self.root.after(100, lambda: self.status_var.set('Hata: eğitim başarısız'))
            self.root.after(100, lambda: messagebox.showerror('Hata', f'Eğitim sırasında hata: {e}'))
    
    def clear(self):
        self.text_input.delete("1.0", tk.END)
        for child in self.results_container.winfo_children():
            child.destroy()

    def _prob_to_hex(self, ai_prob: float) -> str:
        """Convert ai_prob (0..1) to a hex color between green (0) and red (1).
        0 -> green (#008000), 0.5 -> yellowish, 1 -> red (#ff0000)
        """
        # clamp
        p = max(0.0, min(1.0, ai_prob))
        # green -> red interpolation
        g_r = (0, 128, 0)  # dark green
        r_r = (255, 0, 0)  # red
        r = int(g_r[0] + (r_r[0] - g_r[0]) * p)
        g = int(g_r[1] + (r_r[1] - g_r[1]) * p)
        b = int(g_r[2] + (r_r[2] - g_r[2]) * p)
        return f"#{r:02x}{g:02x}{b:02x}"


if __name__ == '__main__':
    root = tk.Tk()
    app = AIDetectorApp(root)
    root.mainloop()
