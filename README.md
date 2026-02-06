# PySongTool

### 🎵 **Music Theory with Python**
**Version**: beta 0.14.0

PySongTool is a Python library designed to help provide information involving music theory

This project follows **SOLID** principles and uses the **Facade** design pattern to organize and simplify the management of classes and functions.

The list of notes is based on the chromatic scale ever using sharps, such as C, C#, D, D#...
the list of note is a LinkedList, which allows the list repeat itself, so we can easily get the next note by adding a number of semitones to the current note, and we can also easily get the previous note by subtracting a number of semitones from the current note. With this implementation, we can easily get intervals like 13th with wourd be out of range in a normal list, but with the LinkedList we can easily get.


---

## 📚 **Requirements**

- Python >= 3.7

---

## 🔧 **Installation**

You can install PySongTool directly from PyPI or locally:

```bash
pip install pysongtool
```

---

## 🗂 **Features**

- Generate chords from a root note and chord name.
- Get all available scales or chords.
- Explore musical intervals based on a root note.
- Retrieve detailed scale information, including notes and associated chords.

---

## 🚀 **How to Use**

### Creating an Instance
```python
from pysongtool import PySongTool

tool = PySongTool()
```
### Generating a Chord
```python
result = tool.chord('C', 'major')
print(result)
# {'chord': 'Cmaj', 'notes': ['C', 'E', 'G']}
```

### Listing All Chords
```python
all_chords = tool.all_chords('C')
print(all_chords)
# [{'maj': {'chord': 'Cmaj', 'notes': ['C', 'E', 'G']}}, ...]
```

### Generating a Scale
```python
scale = tool.scale('C', 'major')
print(scale)
# {'notes': ['C', 'D', 'E', 'F', 'G', 'A', 'B'], 'chords': ['Cmaj', 'Dmin', ...]}
```

### Getting Intervals
```python
intervals = tool.intervals('C')
print(intervals)
# [{'name': 'Unison', 'semitones': 0, 'note': 'C'}, ...]
```

### Calculating Intervals Between Notes
```python
intervals = tool.get_interval('C', 'E', 'G')
print(intervals)
# [{'note': 'E', 'interval': {'name': 'Major Third', 'semitones': 4}}, ...]
```

## 🛠 **Contributing**

Contributions are welcome!

---

## 📝 **License**
This project is licensed under the [MIT License](LICENSE).  

---