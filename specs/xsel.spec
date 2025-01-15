Name:           xsel
Version:        1.2.1
Release:        %autorelease
Summary:        Command line clipboard and X selection tool
License:        HPND-sell-variant
URL:            https://www.vergenet.net/~conrad/software/xsel/

Source0:        https://github.com/kfish/xsel/archive/refs/tags/%{version}.tar.gz#/xsel-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libSM-devel
BuildRequires:  libXext-devel
BuildRequires:  libXt-devel
BuildRequires:  libtool
BuildRequires:  make

%description
XSel is a command line or script utility, similar to xclip, that can copy the
primary and secondary X selection, or any highlighted text, to or from a file,
stdin or stdout. It can also append to and delete the clipboard or buffer that
you would paste with the middle mouse button.

%prep
%autosetup -p1 -C

%build
./autogen.sh --version
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%license COPYING
%doc AUTHORS ChangeLog README
%{_mandir}/man1/xsel.1x*
%{_bindir}/xsel

%changelog
%autochangelog
