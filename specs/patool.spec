Name:           patool
Version:        4.0.2
Release:        %autorelease
Summary:        Portable command line archive file manager

%global forgeurl https://github.com/wummel/patool
%global tag %{version}
%forgemeta

License:        GPL-3.0-or-later
URL:            http://wummel.github.io/patool/
Source:         %forgesource

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  tomcli

BuildRequires:  /usr/bin/7z
BuildRequires:  /usr/bin/7za
# Provided by 7zip in F43+
%if 0%{?fedora} > 42
BuildRequires:  /usr/bin/7zr
BuildRequires:  /usr/bin/7zz
%endif
BuildRequires:  /usr/bin/ar
BuildRequires:  /usr/bin/arc
BuildRequires:  /usr/bin/arj
BuildRequires:  /usr/bin/bsdcpio
BuildRequires:  /usr/bin/bsdtar
BuildRequires:  /usr/bin/bzip2
BuildRequires:  /usr/bin/bzip3
BuildRequires:  /usr/bin/cabextract
BuildRequires:  /usr/bin/compress
BuildRequires:  /usr/bin/cpio
BuildRequires:  /usr/bin/dpkg-deb
BuildRequires:  /usr/bin/extract_chmLib
BuildRequires:  /usr/bin/flac
BuildRequires:  /usr/bin/genisoimage
BuildRequires:  /usr/bin/gzip
BuildRequires:  /usr/bin/isoinfo
BuildRequires:  /usr/bin/jar
BuildRequires:  /usr/bin/lbzip2
BuildRequires:  /usr/bin/lha
BuildRequires:  /usr/bin/lz4
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
BuildRequires:  /usr/bin/unar
BuildRequires:  /usr/bin/unrar
BuildRequires:  /usr/bin/unshar
BuildRequires:  /usr/bin/unzip
BuildRequires:  /usr/bin/xdms
BuildRequires:  /usr/bin/xz
BuildRequires:  /usr/bin/zip
BuildRequires:  /usr/bin/zopfli
BuildRequires:  /usr/bin/zpaq

Requires:       python3-%{name}
Recommends:     python3-%{name}+argcompletion

Recommends:     /usr/bin/7z
Recommends:     /usr/bin/7za
# Provided by 7zip in F43+
%if 0%{?fedora} > 42
Recommends:     /usr/bin/7zr
Recommends:     /usr/bin/7zz
%endif
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
Recommends:     /usr/bin/lha
Recommends:     /usr/bin/lzip
Recommends:     /usr/bin/lzma
Recommends:     /usr/bin/lzop
Recommends:     /usr/bin/mac
Recommends:     /usr/bin/nomarch
Recommends:     /usr/bin/pbzip2
Recommends:     /usr/bin/pigz
Recommends:     /usr/bin/rpm2cpio
Recommends:     /usr/bin/rzip
Recommends:     /usr/bin/shar
Recommends:     /usr/bin/star
Recommends:     /usr/bin/tar
Recommends:     /usr/bin/unrar
Recommends:     /usr/bin/unshar
Recommends:     /usr/bin/unzip
Recommends:     /usr/bin/xdms
Recommends:     /usr/bin/xz
Recommends:     /usr/bin/zip
Recommends:     /usr/bin/zopfli
Recommends:     /usr/bin/zpaq

# Available through RPMFusion
Recommends:     /usr/bin/unace

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

%description %{_description}

%package -n python3-%{name}
Summary:        %{summary}

%description -n python3-%{name} %{_description}

# Add the completion scripts to the extras subpackage.
# While argcompletion is recommended, patool works without it.
%pyproject_extras_subpkg -n python3-patool argcompletion
%config(noreplace) %{bash_completions_dir}/patool.bash
%config(noreplace) %{fish_completions_dir}/patool.fish

%prep
%forgeautosetup -p1

# Upstream switched to setuptools-reproducible, which is not in Fedora.
# Revert to setuptools / setuptools.build_meta
tomcli set pyproject.toml arrays replace \
    build-system.requires 'setuptools-reproducible' 'setuptools'
tomcli set pyproject.toml replace \
    build-system.build-backend 'setuptools_reproducible' 'setuptools.build_meta'

# Unpin argcomplete for older branches
tomcli set pyproject.toml arrays replace \
    project.optional-dependencies.argcompletion 'argcomplete.*' 'argcomplete'

%generate_buildrequires
%pyproject_buildrequires -x argcompletion

%build
%pyproject_wheel

# Create autocompletion shell scripts
register-python-argcomplete --shell bash patool > patool.bash
register-python-argcomplete --shell fish patool > patool.fish

%install
%pyproject_install
%pyproject_save_files %{name}ib
mkdir -p %{buildroot}%{_mandir}/man1/
install -Dpm 0644 doc/patool.1 %{buildroot}%{_mandir}/man1/patool.1

# Install autocompletion shell scripts
%{__install} -D -p -m 0644 patool.bash -t %{buildroot}%{bash_completions_dir}
%{__install} -D -p -m 0644 patool.fish -t %{buildroot}%{fish_completions_dir}

%check
%pytest -r fEs

%files
%license COPYING
%doc README.md doc/*.md doc/changelog.txt
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*

%files -n python3-%{name} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
