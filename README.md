<div align="center">

[<img src="https://github.com/aahan0511/Secrypto/blob/main/assets/icon.png" alt="assets/ascii.png" width=110>](https://github.com/aahan0511/Secrypto "Secrypto on GitHub")

# [**`Secrypto`**](https://github.com/aahan0511/Secrypto "Secrypto on GitHub")

### **`Secrypto`**
**Secrypto** is an excellent cryptographer, with more than $4.5e806$ (**45 with 805 following zeros!**) possible combinations.

---

<br><br>

# **`Contents`**
</div>

* [**`How To Use`**](#how-to-use)
* [**`Installation`**](#installation)
* [**`License`**](#license)
* [**`Contributing`**](#contributing)
* [**`Code Of Conduct`**](#code-of-conduct)
* [**`Security`**](#security)

<br><br>
<div align="center">

# **`How To Use`**

</div>

### **Create a Key**
```python
from Secrypto import Key

key = Key()
```

`Key` can have the following parameters:

- `alterations` (**optional**) (default -> *3*) - This defines the number of alterations for each character.
- `seed` (**optional**) (default -> *None*) - This defines the random seed at which the key will be made

You can also get the `seed` at which the Key is made and the `key` itself.
To get the `key` and the `seed` from the `Key` you can write:

```python
from Secrypto import Key

key = Key()
print(key.key)
print(key.seed)
```

### Encryption and Decryption

When you have the key, it is pretty simple to **encrypt** and **decrypt**.

```python
from Secrypto import Key, encrypt, decrypt

key = Key()

text = "Hello, World"

encryption = encrypt(
    text,
    key
)
print(encryption)

decryption = decrypt(
    encryption,
    key #the same key should be used.
)
print(decryption)

if text == decryption:
    print("success!")
```

<br><br>
<div align="center">

# **`Installation`**

</div>

Write 
```bash
pip install Secrypto
```
Or see the [PyPI page](https://pypi.org/project/secrypto/ "secrypto on PyPI")

<br><br>
<div align="center">

# [**`License`**](https://creativecommons.org/publicdomain/zero/1.0/legalcode.en "CC0 1.0 Universal Website")

</div>

Secrypto is licensed under the [**CC0 1.0 Universal License**](https://github.com/aahan0511/Secrypto/blob/main/LICENSE.md "License for Secrypto").

<br><br>
<div align="center">

# [**`Contributing`**](https://github.com/aahan0511/Secrypto/blob/main/.github/CONTRIBUTING.md "Contributing on Secrypto")

</div>

Follow the [CONTRIBUTING.md](https://github.com/aahan0511/Secrypto/blob/main/.github/CONTRIBUTING.md "Contributing for Secrypto") to ensure a smooth contribution process.

<br><br>
<div align="center">

# [**`Code Of Conduct`**](https://www.contributor-covenant.org/ "Contributor Covenant Website")

</div>

Secrypto has the [**Contributor Covenant Code of Conduct**](https://github.com/aahan0511/Secrypto/blob/main/.github/CODE_OF_CONDUCT.md "Code Of Conduct for Secrypto").

<br><br>
<div align="center">

# [**`Security`**](https://github.com/aahan0511/Secrypto/blob/main/.github/SECURITY.md "Security on Secrypto")

</div>

To view the security and data safety of Secrypto, see [`SECURITY.md`](https://github.com/aahan0511/SecryptoSecrypto/blob/main/.github/SECURITY.md "Security on Secrypto").