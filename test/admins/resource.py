from import_export import resources
from .models import Mahasiswa, Dosen, Matkul, Jadwal, Golongan, Absen, Users

class jadwaltable(resources.ModelResource):
    class Meta:
        model = Jadwal
        fields = ('hari', 'matkul', 'namaDosen', 'golongan', 'ruangan', 'jamMulai', 'jamSelesai')
        export_order = ('hari', 'matkul', 'namaDosen', 'golongan', 'ruangan', 'jamMulai', 'jamSelesai')

class mahasiswatable(resources.ModelResource):
    class Meta:
        model = Mahasiswa
        fields = ('nim', 'nama', 'semester', 'golongan', 'telepon', 'alamat', 'jenisKelamin')
        export_order = ('nim', 'nama', 'semester', 'golongan', 'telepon', 'alamat', 'jenisKelamin')
        
class dosentable(resources.ModelResource):
    class Meta:
        model = Dosen
        fields = ('nip', 'namaDosen')
        export_order = ('nip', 'namaDosen')
        
class matkultable(resources.ModelResource):
    class Meta:
        model = Matkul
        fields = ('kodeMK', 'mataKuliah', 'sks')
        export_order = ('kodeMK', 'mataKuliah', 'sks')