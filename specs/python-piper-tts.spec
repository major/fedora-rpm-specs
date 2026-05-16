Name:           python-piper-tts
Version:        1.4.2
Release:        %autorelease
Summary:        Fast and local neural text-to-speech engine

License:        GPL-3.0-or-later AND MIT
# The main project if GPL 3
#   From the COPYING file and the setup.py file's license= key
# This directory is MIT
#   src/piper/tashkeel/LICENSE

URL:            http://github.com/OHF-voice/piper1-gpl
Source0:        %{url}/archive/v%{version}/piper1-gpl-%{version}.tar.gz

# Need a modified pyproject.toml to convert from scikit-build to scikit-build-core
# Also to have a semi-working setup.py converted pip install so pyproject macros work
Source1:        pyproject.toml

# Modifed the original CMakeList.txt to use system espeak-ng
# There was not much left, so just copy it.
Source2:        CMakeLists.txt

# Does not build on i686 or s390x, no onnxruntime
ExclusiveArch:  x86_64 aarch64 ppc64le

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  espeak-ng-devel
BuildRequires:  ninja-build
BuildRequires:  pytest
BuildRequires:  python3-devel
BuildRequires:  python3dist(flask)
BuildRequires:  python3dist(onnx)
BuildRequires:  python3dist(onnxruntime)
BuildRequires:  python3dist(pathvalidate)

%description
%{summary}.

%package -n     python3-piper-tts
Summary:        Fast and local neural text-to-speech engine

%description -n python3-piper-tts
%{summary}.

%prep
%autosetup -p1 -n piper1-gpl-%{version}

# pyproject.toml
cp -p %{SOURCE1} .
# CMakeLists.txt
cp -p %{SOURCE2} .

# Remove things import complains about
# keep it simple, no training
rm -rf src/piper/train
# no python3-g2pw
rm -f src/piper/phonemize_chinese.py

# Need to change the path to the espeak data
sed -i -e 's@_DIR / "espeak-ng-data"@"/usr/share/espeak-ng-data"@' src/piper/phonemize_espeak.py

# Remove things we do not use to make licensing easier
rm -rf libpiper

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files piper

# move espeak bridge library
# piper is expecting espeakbridge.so, so drop the 'lib'
mv %{buildroot}%{python3_sitearch}/libespeakbridge.so %{buildroot}%{python3_sitearch}/piper/espeakbridge.so

# A wayward c files
rm %{buildroot}%{python3_sitearch}/piper/espeakbridge.c

%check
%pyproject_check_import
# does hookup to espeak-ng-data work ?
# If this this doesn't work, nothing will.
%pytest tests/test_espeak_phonemizer.py
# Other tests
%pytest tests/test_piper.py

%files -n python3-piper-tts
%doc README.md
%license COPYING
%{_bindir}/piper
%{python3_sitearch}/piper/
%{python3_sitearch}/piper_tts-%{version}.dist-info/

%changelog
%autochangelog
