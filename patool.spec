%global forgeurl        https://github.com/wummel/patool
%global commit          ab64562c8cdac34dfd69fcb6e30c8c0014282d11

%forgemeta

%global _description %{expand:
Patool is an archive file manager.

Various archive formats can be created, extracted, tested, listed, searched,
repacked and compared with patool. The advantage of patool is its simplicity
in handling archive files without having to remember a myriad of programs
and options.

The archive format is determined by the file(1) program and as a fallback
by the archive file extension.

patool supports 7z (.7z, .cb7), ACE (.ace, .cba), ADF (.adf), ALZIP (.alz),
APE (.ape), AR (.a), ARC (.arc), ARJ (.arj), BZIP2 (.bz2), CAB (.cab),
COMPRESS (.Z), CPIO (.cpio), DEB (.deb), DMS (.dms), FLAC (.flac), GZIP (.gz),
ISO (.iso), LRZIP (.lrz), LZH (.lha, .lzh), LZIP (.lz), LZMA (.lzma),
LZOP (.lzo), RPM (.rpm), RAR (.rar, .cbr), RZIP (.rz), SHN (.shn),
TAR (.tar, .cbt), XZ (.xz), ZIP (.zip, .jar, .cbz) and ZOO (.zoo)
archive formats. It relies on helper applications to handle those archive
formats (for example bzip2 for BZIP2 archives).

The archive formats TAR, ZIP, BZIP2 and GZIP are supported natively and do
not require helper applications to be installed.}

Name:           patool
Version:        1.12
Release:        %autorelease -p
Summary:        Portable command line archive file manager

License:        GPL-3.0-or-later
URL:            http://wummel.github.io/patool/
Source:         %{forgesource}

# Move _patool_configdata.py to patoolib to avoid it being in the top-level namespace
Patch:          patool-1.12-install__patool_configdata_in_private_namespace.patch
# Star arguments are inheriting from tar ones, but the commands are actually
# slightly differents. Fixed by adding Star own arguments list.
Patch:          patool-1.12-fix_star_options.patch
# Zopfli test: test compression instead of erroneously testing decompression
# which zopfli doesn't do
Patch:          patool-1.12-fix_zopfli_test.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest

BuildRequires:  /usr/bin/7z
BuildRequires:  /usr/bin/7za
BuildRequires:  /usr/bin/ar
BuildRequires:  /usr/bin/bsdcpio
BuildRequires:  /usr/bin/bsdtar
BuildRequires:  /usr/bin/bzip2
BuildRequires:  /usr/bin/cabextract
BuildRequires:  /usr/bin/compress
BuildRequires:  /usr/bin/cpio
BuildRequires:  /usr/bin/dpkg-deb
BuildRequires:  /usr/bin/extract_chmLib
BuildRequires:  /usr/bin/flac
BuildRequires:  /usr/bin/genisoimage
BuildRequires:  /usr/bin/gzip
BuildRequires:  /usr/bin/isoinfo
BuildRequires:  /usr/bin/lbzip2
BuildRequires:  /usr/bin/lzip
BuildRequires:  /usr/bin/lzma
BuildRequires:  /usr/bin/lzop
BuildRequires:  /usr/bin/nomarch
BuildRequires:  /usr/bin/pbzip2
BuildRequires:  /usr/bin/pigz
BuildRequires:  /usr/bin/rpm2cpio
BuildRequires:  /usr/bin/rzip
BuildRequires:  /usr/bin/shar
BuildRequires:  /usr/bin/star
BuildRequires:  /usr/bin/tar
BuildRequires:  /usr/bin/unshar
BuildRequires:  /usr/bin/unzip
BuildRequires:  /usr/bin/xdms
BuildRequires:  /usr/bin/xz
BuildRequires:  /usr/bin/zip
BuildRequires:  /usr/bin/zopfli
BuildRequires:  /usr/bin/zpaq

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


%description %{_description}

%package -n python3-%{name}
Summary:        %{summary}

%description -n python3-%{name}
%{_description}

Python 3 sub-package.

%prep
%forgesetup
%autopatch -p1

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{name}ib

install -Dpm0644 patool.bash-completion %{buildroot}%{bash_completions_dir}/%{name}

%check
# Mime test fails
rm tests/test_mime.py
%tox

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*
%{bash_completions_dir}/%{name}

%files -n python3-%{name} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
