Name:		atool
Version:	0.39.0
Release:	%autorelease
Summary:	A Perl script for managing file archives of various types

License:	GPL-2.0-or-later
URL:		https://www.nongnu.org/atool/
Source0:	https://savannah.nongnu.org/download/%{name}/%{name}-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	bash-completion
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter

%description
atool is a script for managing file archives of various types.

It includes aunpack (to extract archives), apack (to create archives),
als (to list files), acat (to extract files to the standard output),
etc.

atool relies on external programs to handle the archives.
It determines the archive types using file extensions whenever possible,
with a fallback on 'file'.

It includes support for tarballs, Gzip, Bzip, Bzip2, Lzop, Lzma, Pkzip, Rar,
Ace, Arj, RPM, CPIO, Arc, 7z, Alzip.

%prep
%autosetup

# Convert to UTF-8 while keeping the original timestamp
iconv -f iso-8859-1 -t utf-8 NEWS > NEWS.utf8
touch -r NEWS NEWS.utf8
mv NEWS.utf8 NEWS

%build
%configure
%make_build

%install
%make_install
install -Dpm 0644 extra/bash-completion-atool_0.1-1 %{buildroot}%{_datadir}/bash-completion/completions/atool
for f in aunpack arepack apack acat als adiff; do \
    ln -s atool %{buildroot}%{_datadir}/bash-completion/completions/$f; \
done

%check
./atool --version

%files
%license COPYING
%doc NEWS README TODO AUTHORS
%{_bindir}/atool
%{_bindir}/apack
%{_bindir}/aunpack
%{_bindir}/als
%{_bindir}/acat
%{_bindir}/adiff
%{_bindir}/arepack
%{_mandir}/man1/atool.1*
%{_mandir}/man1/apack.1*
%{_mandir}/man1/aunpack.1*
%{_mandir}/man1/als.1*
%{_mandir}/man1/acat.1*
%{_mandir}/man1/adiff.1*
%{_mandir}/man1/arepack.1*
%{_datadir}/bash-completion/completions/a*

%changelog
%autochangelog
