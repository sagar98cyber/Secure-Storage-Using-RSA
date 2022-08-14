# SECURE STORAGE USING RSA_ALGO-PYTHON-SOCKET

>Consider a scenario that the data being stored on the server is not really that secured as we might think. In that case the data being stored is prone to the server attacks and isn't resistant to the attacks at data in transit, data at rest.<br>
>Therefore to protect against that we use RSA algorithm to protect the data in TRANSIT and the data at REST.<br>
<br>

# SCENARIO

>The data being sent on the server is not later on decypted before storing.<br>
>The cipher keys are only stored on the client side.<br>
>Therefore only the client can encrypt or decrypt the data being transferred.<br>
>Thus we try to secure the data at rest and the data in transit<br>
>Example: We try to store a file on server.<br>
>>For that we first save the cipher RSA keys locally.<br>
>>Using these KEYS we encrypt the data before the transfer begins.<br>
>>After retrieving the file we decypt the file using the RSA private key.<br>
<br>

# IMPLEMENTATION

>The file data that is being stored on the remote location is transferred using the PYTHON-SOCKET programming.<br>
>The data stored in the file is encrypted using the RSA ALGORITHM
<br>

# WALKTHROUGH 

[VIDEO TUTORIAL](https://youtu.be/dQ-saITEvpk)

<br>

# FUTURE SCOPE

>The file content amount that could be encrypted is limited due to the limitation in small key size.<br>
>Hence, we can create a business logic that breaks the file size into small chunks that equivalent or less that the keys size or use a better cipher algorithm like the ECC Cipher Algorithm<br>