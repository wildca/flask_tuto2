PRAGMA foreign_keys = OFF;
BEGIN TRANSACTION;
CREATE TABLE "address" (
  "id"     INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  "street" TEXT                              NOT NULL,
  "city"   TEXT                              NOT NULL
);
CREATE TABLE user (
  "id"         INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  "name"       TEXT                              NOT NULL,
  "email"      TEXT                              NOT NULL,
  "nick"       TEXT,
  "address_id" INTEGER,
  FOREIGN KEY (address_id) REFERENCES address (id)
);
COMMIT;
