Name:		unrtf
Summary:	RTF (Rich Text Format) to other formats converter
Version:	0.21.10
Release:	%autorelease
License:	GPL-3.0-or-later
URL:		https://www.gnu.org/software/unrtf
Source0:	https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
Source1:	https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz.sig
# gpg --no-default-keyring --keyring ./keyring.gpg --keyserver keyserver.ubuntu.com --recv-key 46EA854F5FC5F5A0A9D2BFE89175BF0B3EC83090
# gpg --no-default-keyring --keyring ./keyring.gpg --output 46EA854F5FC5F5A0A9D2BFE89175BF0B3EC83090.gpg --export
Source2:	46EA854F5FC5F5A0A9D2BFE89175BF0B3EC83090.gpg
Patch:		0001-Adjust-malloc-types.patch
BuildRequires:	automake
BuildRequires:	gcc
BuildRequires:	gnupg2
BuildRequires:	make

%description
UnRTF is a command-line program written in C which converts documents in
Rich Text Format (.rtf) to HTML, LaTeX, troff macros, and RTF itself.
Converting to HTML, it supports a number of features of Rich Text Format:
    * Changes in the text's font, size, weight (bold), and slant (italic)
    * Underlines and strikethroughs
    * Partial support for text shadowing, outlining, embossing, or engraving
    * Capitalizations
    * Superscripts and subscripts
    * Expanded and condensed text
    * Changes in the foreground and background colors
    * Conversion of special characters to HTML entities

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
autoreconf -ivf
%configure
%make_build

%install
%make_install

%check
make check

%files
%doc README ChangeLog AUTHORS NEWS
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/*
%{_datadir}/%{name}/

%changelog
%autochangelog
