%global desc Patool is an archive file manager. \
\
Various archive formats can be created, extracted, tested, listed, searched, \
repacked and compared with patool. The advantage of patool is its simplicity \
in handling archive files without having to remember a myriad of programs \
and options. \
\
The archive format is determined by the file(1) program and as a fallback \
by the archive file extension. \
\
patool supports 7z (.7z, .cb7), ACE (.ace, .cba), ADF (.adf), ALZIP (.alz), \
APE (.ape), AR (.a), ARC (.arc), ARJ (.arj), BZIP2 (.bz2), CAB (.cab), \
COMPRESS (.Z), CPIO (.cpio), DEB (.deb), DMS (.dms), FLAC (.flac), GZIP (.gz), \
ISO (.iso), LRZIP (.lrz), LZH (.lha, .lzh), LZIP (.lz), LZMA (.lzma), \
LZOP (.lzo), RPM (.rpm), RAR (.rar, .cbr), RZIP (.rz), SHN (.shn), \
TAR (.tar, .cbt), XZ (.xz), ZIP (.zip, .jar, .cbz) and ZOO (.zoo) \
archive formats. It relies on helper applications to handle those archive \
formats (for example bzip2 for BZIP2 archives).\
\
The archive formats TAR, ZIP, BZIP2 and GZIP are supported natively and do \
not require helper applications to be installed.


Name:           patool
Version:        1.12
Release:        22%{?dist}
Summary:        Portable command line archive file manager

License:        GPLv3+
URL:            http://wummel.github.io/patool/
Source0:        https://github.com/wummel/patool/archive/upstream/%{version}/%{name}-%{version}.tar.gz

# Move _patool_configdata.py to patoolib to avoid it being in the top-level namespace
Patch0:         patool-1.12-install__patool_configdata_in_private_namespace.patch
# Star arguments are inheriting from tar ones, but the commands are actually
# slightly differents. Fixed by adding Star own arguments list.
Patch1:         patool-1.12-fix_star_options.patch
# Zopfli test: test compression instead of erroneously testing decompression
# which zopfli doesn't do
Patch2:         patool-1.12-fix_zopfli_test.patch

BuildArch:      noarch

BuildRequires:     /usr/bin/7z
BuildRequires:     /usr/bin/7za
BuildRequires:     /usr/bin/ar
BuildRequires:     /usr/bin/bsdcpio
BuildRequires:     /usr/bin/bsdtar
BuildRequires:     /usr/bin/bzip2
BuildRequires:     /usr/bin/cabextract
BuildRequires:     /usr/bin/compress
BuildRequires:     /usr/bin/cpio
BuildRequires:     /usr/bin/dpkg-deb
BuildRequires:     /usr/bin/extract_chmLib
BuildRequires:     /usr/bin/flac
BuildRequires:     /usr/bin/genisoimage
BuildRequires:     /usr/bin/gzip
BuildRequires:     /usr/bin/isoinfo
BuildRequires:     /usr/bin/lbzip2
BuildRequires:     /usr/bin/lzip
BuildRequires:     /usr/bin/lzma
BuildRequires:     /usr/bin/lzop
BuildRequires:     /usr/bin/nomarch
BuildRequires:     /usr/bin/pbzip2
BuildRequires:     /usr/bin/pigz
BuildRequires:     /usr/bin/rpm2cpio
BuildRequires:     /usr/bin/rzip
BuildRequires:     /usr/bin/shar
BuildRequires:     /usr/bin/star
BuildRequires:     /usr/bin/tar
BuildRequires:     /usr/bin/unshar
BuildRequires:     /usr/bin/unzip
BuildRequires:     /usr/bin/xdms
BuildRequires:     /usr/bin/xz
BuildRequires:     /usr/bin/zip
BuildRequires:     /usr/bin/zopfli
BuildRequires:     /usr/bin/zpaq

Requires:       python3-%{name}

Recommends:     /usr/bin/7z
Recommends:     /usr/bin/7za
Recommends:     /usr/bin/ar
Recommends:     /usr/bin/bsdcpio
Recommends:     /usr/bin/bsdtar
Recommends:     /usr/bin/bzip2
Recommends:     /usr/bin/cabextract
Recommends:     /usr/bin/compress
Recommends:     /usr/bin/cpio
Recommends:     /usr/bin/dpkg-deb
Recommends:     /usr/bin/extract_chmLib
Recommends:     /usr/bin/flac
Recommends:     /usr/bin/genisoimage
Recommends:     /usr/bin/gzip
Recommends:     /usr/bin/isoinfo
Recommends:     /usr/bin/lbzip2
Recommends:     /usr/bin/lzip
Recommends:     /usr/bin/lzma
Recommends:     /usr/bin/lzop
Recommends:     /usr/bin/nomarch
Recommends:     /usr/bin/pbzip2
Recommends:     /usr/bin/pigz
Recommends:     /usr/bin/rpm2cpio
Recommends:     /usr/bin/rzip
Recommends:     /usr/bin/shar
Recommends:     /usr/bin/star
Recommends:     /usr/bin/tar
Recommends:     /usr/bin/unshar
Recommends:     /usr/bin/unzip
Recommends:     /usr/bin/xdms
Recommends:     /usr/bin/xz
Recommends:     /usr/bin/zip
Recommends:     /usr/bin/zopfli
Recommends:     /usr/bin/zpaq

# Available through RPMFusion
Recommends:     /usr/bin/lha
Recommends:     /usr/bin/mac
Recommends:     /usr/bin/unace
Recommends:     /usr/bin/unrar

# Not available in Fedora
# Recommends:     /usr/bin/lcab
# Recommends:     /usr/bin/lhasa
# Recommends:     /usr/bin/rar
# Recommends:     /usr/bin/unadf
# Recommends:     /usr/bin/unalz
# Recommends:     /usr/bin/zoo

# Planned
# Recommends:     /usr/bin/clzip
# Recommends:     /usr/bin/lrzip
# Recommends:     /usr/bin/pdlzip
# Recommends:     /usr/bin/plzip

# Python 2 only
# Recommends:     /usr/bin/archmage


%description
%{desc}


%package -n python3-%{name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{name}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest

%description -n python3-%{name}
%{desc}

Python 3 sub-package.


%prep
%autosetup -p1 -n %{name}-upstream-%{version}


%build
%py3_build


%install
%py3_install

install -Dpm0644 patool.bash-completion \
    %{buildroot}%{_datadir}/bash-completion/completions/patool


%check
# Mime test fails
rm tests/test_mime.py
PYTHONPATH=. pytest-3 -v tests


%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_datadir}/bash-completion/completions/patool
%{_mandir}/man1/%{name}.1.*


%files -n python3-%{name}
%license COPYING
%doc README.md
%{python3_sitelib}/patoolib
%{python3_sitelib}/%{name}-%{version}-py%{python3_version}.egg-info


%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.12-21
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.12-18
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.12-15
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.12-12
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.12-10
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.12-9
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 14 14:12:12 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.12-7
- Disable Archmage which is Python 2 only

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 17 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.12-5
- Drop Python 2 subpackage

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.12-3
- Rebuilt for Python 3.7

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.12-2
- Rebuilt for Python 3.7

* Fri Feb 02 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.12-1
- First RPM release
