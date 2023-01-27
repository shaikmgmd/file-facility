$dependences = @("tkinter", "cx_freeze", "tkintertable", "tkcalendar")

foreach($dependence in $dependences) {
    pip install $dependence
}
