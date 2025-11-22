#!/usr/bin/env python3
#
# zeta_prg.py — short description
#
# Copyright (C) 2025 Rasto Vojtko <rastislav.vojtko@gmail.com>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#  
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#  
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
# 
# SPDX-License-Identifier: GPL-3.0-or-later
# 

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import zeta # type: ignore

APP_VERSION = "0.9.0-Alpha"
APP_NAME = "Zeta Tk"
DATE = "2025-11-22"

class Zeta(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root)
        self.root = root
        self.pack()
    
        # CONSTANTS FOR ZETA CALCULATION
        self.lambda_a = tk.DoubleVar(value=zeta.lambda_a)         # decay constant 238U [yr^-1]
        self.lambda_a_err = tk.DoubleVar(value=zeta.lambda_a_err) # error of decay constant 238U [yr^-1]
        self.g = tk.DoubleVar(value=zeta.g)                       # geometric factor (0.5 = external detector)

        # VARIABLES FOR ZETA CALCULATION
        self.nd = tk.StringVar()
        self.nd_area = tk.DoubleVar()
        self.rod = tk.DoubleVar()

        self.ns = tk.IntVar()
        self.ns_area = tk.DoubleVar()
        self.ros = tk.DoubleVar()

        self.ni = tk.IntVar()        
        self.ni_area = tk.DoubleVar()
        self.roi = tk.DoubleVar()

        self.ns_ni = tk.DoubleVar()
        self.ns_ni_area = tk.DoubleVar()
        self.ns_ni_ro = tk.DoubleVar() 

        self.zeta_value = tk.DoubleVar()
        self.zeta_err = tk.DoubleVar()  
        self.zeta_perc = tk.DoubleVar()

        self.std = zeta.standards.values()
        print(self.std)
        self.names = [f"{item[0]} ({item[1]}±{item[2]} Ma)" for item in self.std]
        print(self.names)

        self.create_widgets()


    def create_widgets(self):
        # --- Title Label ---
        title_label = ttk.Label(self, text="Zeta Factor Calculation", \
                                justify=tk.LEFT, font=("Arial", 12, "bold"), foreground="blue")
        title_label.grid(row=0, column=0, columnspan=5, pady=10)

        # --- Set LabelFrame ---
        set_frame = ttk.LabelFrame(self, text=' Constants... ')
        set_frame.grid(row=1, column=0, columnspan=5, sticky="we", padx=5, pady=5)

        self.mineral_combo = ttk.Combobox(set_frame, values=list(zeta.minerals.values()), width=32)
        self.mineral_combo.grid(row=0, column=0, sticky=tk.W, padx=5)
        self.mineral_combo.current(0)  

        self.standard_combo = ttk.Combobox(set_frame, values=self.names, width=32)
        self.standard_combo.grid(row=1, column=0, sticky=tk.W, padx=5)
        self.standard_combo.current(2)   

        lambda_a_lbl = ttk.Label(set_frame, text='λ (238U) [yr^-1]: ')
        lambda_a_lbl.grid(row=0, column=2, sticky=tk.W, padx=5)

        lambda_a_err_lbl = ttk.Label(set_frame, text='σ(λ) [yr^-1]: ')
        lambda_a_err_lbl.grid(row=1, column=2, sticky=tk.W, padx=5)

        g_lbl = ttk.Label(set_frame, text='Geometric factor g: ')
        g_lbl.grid(row=2, column=2, sticky=tk.W, padx=5) 

        lambda_a_entry = tk.Entry(set_frame, width=15, textvariable=self.lambda_a, justify=tk.RIGHT, bg='white')
        lambda_a_entry.grid(row=0, column=3, sticky=tk.W, padx=5, pady=5)

        lambda_a_err_entry = tk.Entry(set_frame, width=15, textvariable=self.lambda_a_err, justify=tk.RIGHT, bg='white')
        lambda_a_err_entry.grid(row=1, column=3, sticky=tk.W, padx=5, pady=5)

        self.g_entry = tk.Entry(set_frame, width=15, textvariable=self.g, justify=tk.RIGHT, bg='white')
        self.g_entry.grid(row=2, column=3, sticky=tk.W, padx=5, pady=5)  


        # --- Input LabelFrame ------------------------------------------------
        input_frame = ttk.LabelFrame(self, text=' Insert values... ')
        input_frame.grid(row=2, column=0, columnspan=5, sticky="we", padx=5, pady=5)

        # --- Nd entries ---
        nd_lbl = ttk.Label(input_frame, text='Nd: ')
        nd_lbl.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.nd_entry = tk.Entry(input_frame, width=12, justify=tk.RIGHT, textvariable=self.nd, bg='white')
        self.nd_entry.grid(row=0, column=1, sticky="W, E", padx=5, pady=5)
        self.nd_entry.delete(0, tk.END)
        self.nd_entry.focus()
        nd_area_lbl = ttk.Label(input_frame, text='Nd area: ')
        nd_area_lbl.grid(row=0, column=2, sticky=tk.W, padx=5, pady=5)
        nd_area_entry = tk.Entry(input_frame, width=12, justify=tk.RIGHT, textvariable=self.nd_area, bg='white')
        nd_area_entry.grid(row=0, column=3, sticky="W, E", padx=5, pady=5)
        nd_area_entry.delete(0, tk.END)
        nd_area_entry.config(state='disabled')
        nd_ro_lbl = ttk.Label(input_frame, text='ρd: ')
        nd_ro_lbl.grid(row=0, column=4, sticky=tk.W, padx=5, pady=5)
        self.nd_ro_entry = tk.Entry(input_frame, width=12, justify=tk.RIGHT, textvariable=self.rod, bg='white')
        self.nd_ro_entry.grid(row=0, column=5, sticky="W, E", padx=5, pady=5)
        self.nd_ro_entry.delete(0, tk.END)

        # --- Ns entries ---
        ns_lbl = ttk.Label(input_frame, text='Ns: ')
        ns_lbl.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.ns_entry = tk.Entry(input_frame, width=12, justify=tk.RIGHT, textvariable=self.ns, bg='white')
        self.ns_entry.grid(row=1, column=1, sticky="W, E", padx=5, pady=5)
        self.ns_entry.delete(0, tk.END)
        ns_area_lbl = ttk.Label(input_frame, text='Ns area (cm\u00B2): ')
        ns_area_lbl.grid(row=1, column=2, sticky=tk.W, padx=5, pady=5)
        self.ns_area_entry = tk.Entry(input_frame, width=12, justify=tk.RIGHT, textvariable=self.ns_area, bg='white')
        self.ns_area_entry.grid(row=1, column=3, sticky="W, E", padx=5, pady=5)
        self.ns_area_entry.delete(0, tk.END)
        ns_ro_lbl = ttk.Label(input_frame, text='ρs^6: ')
        ns_ro_lbl.grid(row=1, column=4, sticky=tk.W, padx=5, pady=5)
        self.ns_ro_entry = tk.Entry(input_frame, width=12, justify=tk.RIGHT, textvariable=self.ros, bg='white')
        self.ns_ro_entry.grid(row=1, column=5, sticky="W, E", padx=5, pady=5)
        self.ns_ro_entry.delete(0, tk.END)
        self.ns_ro_entry.config(state='disabled')

        # --- Ni entries ---
        ni_lbl = ttk.Label(input_frame, text='Ni: ')
        ni_lbl.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        self.ni_entry = tk.Entry(input_frame, width=10, justify=tk.RIGHT, textvariable=self.ni, bg='white')
        self.ni_entry.grid(row=2, column=1, sticky="W, E", padx=5, pady=5)
        self.ni_entry.delete(0, tk.END)
        ni_area_lbl = ttk.Label(input_frame, text='Ni area (cm\u00B2): ')
        ni_area_lbl.grid(row=2, column=2, sticky=tk.W, padx=5, pady=5)
        self.ni_area_entry = tk.Entry(input_frame, width=12, justify=tk.RIGHT, textvariable=self.ni_area, bg='white')
        self.ni_area_entry.grid(row=2, column=3, sticky="W, E", padx=5, pady=5)
        self.ni_area_entry.delete(0, tk.END)
        ni_ro_lbl = ttk.Label(input_frame, text='ρi^6: ')
        ni_ro_lbl.grid(row=2, column=4, sticky=tk.W, padx=5, pady=5)
        self.ni_ro_entry = tk.Entry(input_frame, width=12, justify=tk.RIGHT, textvariable=self.roi, bg='white')
        self.ni_ro_entry.grid(row=2, column=5, sticky="W, E", padx=5, pady=5)
        self.ni_ro_entry.delete(0, tk.END) 
        self.ni_ro_entry.config(state='disabled') 

        # --- Ns/Ni entries ---
        ns_ni_lbl = ttk.Label(input_frame, text='Ns/Ni: ')
        ns_ni_lbl.grid(row=3, column=0, sticky=tk.W, padx=5, pady=5) 
        self.ns_ni_entry = tk.Entry(input_frame, width=10, justify=tk.RIGHT, textvariable=self.ns_ni, bg='white')
        self.ns_ni_entry.grid(row=3, column=1, sticky="W, E", padx=5, pady=5)
        self.ns_ni_entry.delete(0, tk.END)
        self.ns_ni_entry.config(state='disabled')
        ns_ni_area_lbl = ttk.Label(input_frame, text='Ns/Ni area: ')
        ns_ni_area_lbl.grid(row=3, column=2, sticky=tk.W, padx=5, pady=5)
        ns_ni_area_entry = tk.Entry(input_frame, width=12, justify=tk.RIGHT, textvariable=self.ns_ni_area, bg='white')
        ns_ni_area_entry.grid(row=3, column=3, sticky="W, E", padx=5, pady=5)
        ns_ni_area_entry.delete(0, tk.END) 
        ns_ni_area_entry.config(state='disabled')
        ns_ni_ro_lbl = ttk.Label(input_frame, text='ρs/ρi: ')
        ns_ni_ro_lbl.grid(row=3, column=4, sticky=tk.W, padx=5, pady=5)
        self.ns_ni_ro_entry = tk.Entry(input_frame, width=12, justify=tk.RIGHT, textvariable=self.ns_ni_ro, bg='white')
        self.ns_ni_ro_entry.grid(row=3, column=5, sticky="W, E", padx=5, pady=5)
        self.ns_ni_ro_entry.delete(0, tk.END)    
        self.ns_ni_ro_entry.config(state='disabled')
       

        # --- Output LabelFrame ---
        output_frame = ttk.LabelFrame(self, text=' Zeta value... ')
        output_frame.grid(row=3, column=0, columnspan=5, sticky="we", padx=5, pady=5)

        # --- Zeta entries ---
        zeta_lbl = ttk.Label(output_frame, text='ζ (Ma/cm^2): ')
        zeta_lbl.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.zeta_entry = tk.Entry(output_frame, width=7, justify=tk.RIGHT, textvariable=self.zeta_value, \
                                   font=("Arial", 11, "bold"), bg='lightyellow')
        self.zeta_entry.grid(row=0, column=1, sticky="W, E", padx=5, pady=5, ipady=6)
        self.zeta_entry.delete(0, tk.END)
        self.zeta_entry.config(state='disabled')
        zeta_err_lbl = ttk.Label(output_frame, text='σ(ζ) (Ma/cm^2): ')
        zeta_err_lbl.grid(row=0, column=2, sticky=tk.W, padx=5, pady=5)
        self.zeta_err_entry = tk.Entry(output_frame, width=7, justify=tk.RIGHT, textvariable=self.zeta_err, \
                                       font=("Arial", 11, "bold"), bg='lightyellow')
        self.zeta_err_entry.grid(row=0, column=3, sticky="W, E", padx=5, pady=5, ipady=6)
        self.zeta_err_entry.delete(0, tk.END)
        self.zeta_err_entry.config(state='disabled')

        zeta_perc_lbl = ttk.Label(output_frame, text='σ(ζ) (%): ')
        zeta_perc_lbl.grid(row=0, column=4, sticky=tk.W, padx=5, pady=5)
        self.zeta_perc_entry = tk.Entry(output_frame, width=7, justify=tk.RIGHT, textvariable=self.zeta_perc, \
                                       font=("Arial", 11, "bold"), bg='lightyellow')
        self.zeta_perc_entry.grid(row=0, column=5, sticky="W, E", padx=5, pady=5, ipady=6)
        self.zeta_perc_entry.delete(0, tk.END)
        self.zeta_perc_entry.config(state='disabled')


        # --- Calculate Button ---
        calc_button = ttk.Button(self, text="Calculate ζ", command=self.calculate_zeta)
        calc_button.grid(row=4, column=0, pady=10)

        clear_button = ttk.Button(self, text="Clear all", command=self.clear_all)
        clear_button.grid(row=4, column=1, pady=10) 
    
    def clear_all(self):
        # --- Clear all input and output entries ---
        self.nd_entry.delete(0, tk.END)
        self.nd_ro_entry.delete(0, tk.END)

        self.ns_entry.delete(0, tk.END)
        self.ns_area_entry.delete(0, tk.END)
        self.ns_ro_entry.config(state='normal')
        self.ns_ro_entry.delete(0, tk.END)
        self.ns_ro_entry.config(state='disabled')

        self.ni_entry.delete(0, tk.END)
        self.ni_area_entry.delete(0, tk.END)
        self.ni_ro_entry.config(state='normal')
        self.ni_ro_entry.delete(0, tk.END)
        self.ni_ro_entry.config(state='disabled')

        self.ns_ni_entry.config(state='normal')
        self.ns_ni_entry.delete(0, tk.END)
        self.ns_ni_entry.config(state='disabled')

        self.ns_ni_ro_entry.config(state='normal')
        self.ns_ni_ro_entry.delete(0, tk.END)
        self.ns_ni_ro_entry.config(state='disabled')

        self.zeta_entry.config(state='normal')
        self.zeta_entry.delete(0, tk.END)
        self.zeta_entry.config(state='disabled')
        self.zeta_err_entry.config(state='normal')
        self.zeta_err_entry.delete(0, tk.END)
        self.zeta_err_entry.config(state='disabled')
        self.zeta_perc_entry.config(state='normal')
        self.zeta_perc_entry.delete(0, tk.END)
        self.zeta_perc_entry.config(state='disabled')

    def calculate_zeta(self):
        # --- Validate inputs ---
        try:
            lambda_a = float(self.lambda_a.get())
            lambda_a_err = float(self.lambda_a_err.get())
            if lambda_a <= 0 or lambda_a_err < 0:
                raise ValueError("Lambda values must be positive.") 
            #print(f"Lambda_a: {self.lambda_a}, type: {type(self.lambda_a)}")
        except (tk.TclError, ValueError):
            messagebox.showerror(
            "Chybný vstup",
            "Zadaná neplatná hodnota  rozpadovej konštanty λ alebo jej chyby σ(λ).\nHodnoty musia byť kladné čísla (float)."
            ) 
            return

        try:
            g = float(self.g.get())
            if g <= 0 or g > 1:
                raise ValueError("g must be in the interval (0, 1].")
            self.g_entry.config(bg="white")
        except (tk.TclError, ValueError):
            self.g_entry.config(bg="tomato")
            messagebox.showerror(
            "Chybný vstup",
            "Zadaná neplatná hodnota  geometrického faktoru (g).\nHodnota musí byť číslo (float) v intervale (0, 1], default g=0.5."
            )   

        # --- Validate Nd and ρd ---
        try:
            nd = int(self.nd.get())
            self.nd_entry.config(bg="white")
        except (tk.TclError, ValueError):
            self.nd_entry.config(bg="tomato")
            messagebox.showerror(
            "Chybný vstup",
            "Zadaná neplatná hodnota Nd.\nHodnota musí byť celé číslo (integer)."
            )

        try:
            rod = float(self.rod.get())
            self.nd_ro_entry.config(bg="white") 
        except (tk.TclError, ValueError):
            self.nd_ro_entry.config(bg="tomato")
            messagebox.showerror(
            "Chybný vstup",
            "Zadaná neplatná hodnota ρd.\nHodnota musí byť číslo (float)."
            )   

        # --- Validate Ns and Ns area ---
        try:
            ns = int(self.ns.get())
            self.ns_entry.config(bg="white")
        except (tk.TclError, ValueError):
            self.ns_entry.config(bg="tomato")
            messagebox.showerror(
            "Chybný vstup",
            "Zadaná neplatná hodnota Ns.\nHodnota musí byť celé číslo (integer)."
            )
        
        try:
            ns_area = float(self.ns_area.get())
            self.ns_area_entry.config(bg="white")   
        except (tk.TclError, ValueError):
            self.ns_area_entry.config(bg="tomato")
            messagebox.showerror(
            "Chybný vstup",
            "Zadaná neplatná hodnota plochy Ns (cm^2).\nHodnota musí byť číslo (float)."
            )

        # --- Validate Ni and Ni area ---
        try:
            ni = int(self.ni.get())
            self.ni_entry.config(bg="white")    
        except (tk.TclError, ValueError):
            self.ni_entry.config(bg="tomato")
            messagebox.showerror(
            "Chybný vstup",
            "Zadaná neplatná hodnota Ni.\nHodnota musí byť celé číslo (integer)."
            )

        try:
            ni_area = float(self.ni_area.get())
            self.ni_area_entry.config(bg="white")   
        except (tk.TclError, ValueError):
            self.ni_area_entry.config(bg="tomato")
            messagebox.showerror(
            "Chybný vstup",
            "Zadaná neplatná hodnota plochy Ni (cm^2).\nHodnota musí byť číslo (float)."
            )

        # --- Calculate Ns/Ni and update entry --- 
        ns_ni = ns / ni  
        self.ns_ni_entry.config(state='normal')
        self.ns_ni_entry.delete(0, tk.END)
        self.ns_ni_entry.insert(tk.END, f"{ns_ni:.6f}")
        self.ns_ni_entry.config(state='disabled')

        # --- Calculate ros and update entry --- 
        ros = (ns / ns_area) / 1e6
        self.ns_ro_entry.config(state='normal')
        self.ns_ro_entry.delete(0, tk.END)
        self.ns_ro_entry.insert(tk.END, f"{ros:.6f}")
        self.ns_ro_entry.config(state='disabled')

        # --- Calculate roi and update entry ---
        roi = (ni / ni_area) / 1e6
        self.ni_ro_entry.config(state='normal') 
        self.ni_ro_entry.delete(0, tk.END)
        self.ni_ro_entry.insert(tk.END, f"{roi:.6f}")
        self.ni_ro_entry.config(state='disabled')

        # --- Calculate ns/ni ro and update entry ---
        ns_ni_ro = ros / roi
        self.ns_ni_ro_entry.config(state='normal')  
        self.ns_ni_ro_entry.delete(0, tk.END)
        self.ns_ni_ro_entry.insert(tk.END, f"{ns_ni_ro:.6f}")
        self.ns_ni_ro_entry.config(state='disabled')

        mineral = self.mineral_combo.get()
        print(f"Selected mineral: {mineral}")
        std = self.standard_combo.get()
        print(f"Selected standard: {std}")     
        
        # --- Identify standard code ---
        if "Fish Canyon" in std:
            print("Použili sme štandard Fish Canyon Tuff.")
            std_code = "FCT"
        elif "Duluth Complex" in std:
            print("Použili sme štandard Duluth Complex.")
            std_code = "FC1"
        elif "Durango" in std:
            print("Použili sme štandard Durango.")
            std_code = "DUR"
        elif "Mount Dromedary" in std:
            print("Použili sme štandard Mount Dromedary.")
            std_code = "MD"
        elif "Mount McClure" in std:
            print("Použili sme štandard Mount McClure.")
            std_code = "MM"
        elif "TEMORA2" in std:
            print("Použili sme štandard TEMORA2.")
            std_code = "TEM2"
        elif "Tardree Rhyolite" in std:
            print("Použili sme štandard Tardree Rhyolite.")
            std_code = "TR"
        else:
            messagebox.showerror(
            "Chybný vstup",
            "Zadaná neplatná hodnota štandardu."
            ) 
            return
        
        print(f"CODE: {std_code} and type: {type(std_code)}") 

        # --- Test whether standard and mineral are compatible ---
        std_params = zeta.standards[std_code] 
        print(std_params)  
        if mineral == "Apatite" and not std_params[3]:
            messagebox.showerror(
            "Chybný vstup",
            f"Štandard {std_params[0]} nie je vhodný pre minerál Apatite."
            ) 
            return
        if mineral == "Zircon" and not std_params[4]:
            messagebox.showerror(
            "Chybný vstup",
            f"Štandard {std_params[0]} nie je vhodný pre minerál Zircon."
            ) 
            return
        if mineral == "Titanite" and not std_params[5]:
            messagebox.showerror(
            "Chybný vstup",
            f"Štandard {std_params[0]} nie je vhodný pre minerál Titanite."
            ) 
            return
        
        ros = float(self.ros.get())
        roi = float(self.roi.get())
        rod = float(self.rod.get())


        # --- Calculate zeta ---
        result = zeta.calc_zeta(std_code, mineral, lambda_a, lambda_a_err, 
                       g, nd, ns, ni, ros, roi, rod)
        
        print(result)


        # --- Update output entries ---        
        self.zeta_entry.config(state='normal')
        self.zeta_entry.delete(0, tk.END)
        self.zeta_entry.insert(tk.END, f"{result['zeta_user']:.2f}")
        #self.zeta_entry.config(state='disabled')
        self.zeta_err_entry.config(state='normal')
        self.zeta_err_entry.delete(0, tk.END)
        self.zeta_err_entry.insert(tk.END, f"{result['sigma_zeta']:.2f}")
        #self.zeta_err_entry.config(state='disabled')
        self.zeta_perc_entry.config(state='normal')
        self.zeta_perc_entry.delete(0, tk.END)
        self.zeta_perc_entry.insert(tk.END, f"{result['rel_sigma_percent']:.2f}")
        #self.zeta_perc_entry.config(state='disabled')

        # --- Print results to console ---
        print(f"Zeta (user equation): {result['zeta_user']:.2f}")
        # print(f"Zeta (Hurford & Green): {zeta_HG:.4e}")
        # print(f"Recalculated age: {t_calc_Ma:.2f} Ma")
        print(f"Uncertainty of Zeta: {result['sigma_zeta']:.2f}")
        print(f"Relative uncertainty: {result['rel_sigma_percent']:.2f} %")
        

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('500x450+200+200')
    root.title("Zeta Tk v. " + APP_VERSION + " Experimental prototype")
    #root.iconbitmap('geolcalc.ico')
    print("Package {} v. {} - {} was setting up successfully.".format(APP_NAME, APP_VERSION, DATE))

    app = Zeta(root)

    root.mainloop()

# End of script (c) Rasto Vojtko
