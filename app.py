from pygrabber.dshow_graph import FilterGraph
from tkinter import Tk, Button, Label, Checkbutton, messagebox, IntVar

def configure(i: int, device: str, cam_on: IntVar) -> None:
    graph = FilterGraph()
    try:
        graph.add_video_input_device(i)
        if cam_on.get() == 1:
            graph.add_default_render()
            graph.prepare_preview_graph()
        graph.run()
        graph.get_input_device().set_properties()
    except Exception as e:
        messagebox.showerror("Error", f"Couldn't open {device}: {e})")
    finally:
        graph.stop()
        graph.remove_filters()

def main() -> None:
    root = Tk()
    root.title("CamControl")
    devices = FilterGraph().get_input_devices()
    Label(root, text="Select a camera to configure.").pack(pady=20)
    cam_on = IntVar()
    Checkbutton(root, text="Enable camera preview (ensure no other app is using the camera).", variable=cam_on, onvalue=1, offvalue=0).pack(pady=10)
    if not devices:
        Label(root, text="No camera/video capture device found.").pack(pady=10)
    else:
        for i, device in enumerate(devices):
            Button(root, text=device, anchor="w", command=lambda i=i, device=device, cam_on=cam_on: configure(i, device, cam_on)).pack(pady=10)
    root.mainloop()

if __name__ == "__main__":
    main()
