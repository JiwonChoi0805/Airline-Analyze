// #include <LiquidCrystal.h>

// LiquidCrystal lcd(3, 4, 10, 11, 12, 13);

void setup() {
    lcd.begin(16, 2);
    lcd.clear();
}

void loop() {
    for (int i = 0; i < 3; i++) {  // 수정: 1을 i < 3로 변경
        lcd.setCursor(i, 0);
        lcd.print("Hello Hopy!");
        delay(1000);
        lcd.clear();
    }
    lcd.setCursor(0, 1);
    lcd.print("Hello Hopy!");
    delay(1000);
    lcd.clear();
}
