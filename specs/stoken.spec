Name:           stoken
Version:        0.93
Release:        %autorelease
Summary:        Token code generator compatible with RSA SecurID 128-bit (AES) token
License:        LGPL-2.1-or-later
URL:            https://github.com/stoken-dev/stoken

Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(hogweed) >= 2.4
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(nettle) >= 2.4

%description
Software Token for Linux/UNIX. It's a token code generator compatible with RSA
SecurID 128-bit (AES) tokens. It is a hobbyist project, not affiliated with or
endorsed by RSA Security.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{_isa} = %{version}-%{release}

%description devel
Software Token for Linux/UNIX. It's a token code generator compatible with RSA
SecurID 128-bit (AES) tokens. It is a hobbyist project, not affiliated with or
endorsed by RSA Security.

This package provides the development files for %{name}.

%package libs
Summary:        Libraries for %{name}

%description libs
Software Token for Linux/UNIX. It's a token code generator compatible with RSA
SecurID 128-bit (AES) tokens. It is a hobbyist project, not affiliated with or
endorsed by RSA Security.

This package contains %{name} libraries.

%package cli
Summary:        Command line tool for %{name}

%description cli
Software Token for Linux/UNIX. It's a token code generator compatible with RSA
SecurID 128-bit (AES) tokens. It is a hobbyist project, not affiliated with or
endorsed by RSA Security.

This package contains the command line tool for %{name}.

%package gui
Summary:        Graphical interface program for %{name}

%description gui
Software Token for Linux/UNIX. It's a token code generator compatible with RSA
SecurID 128-bit (AES) tokens. It is a hobbyist project, not affiliated with or
endorsed by RSA Security.

This package contains the graphical interface program for %{name}.

%prep
%autosetup

%build
autoreconf -v -f --install
%configure --with-gtk --disable-static
%make_build

%install
%make_install

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}-gui.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}-gui-small.desktop
make check

# Remove stuff we don't need
find %{buildroot} -type f -name "*.la" -delete
rm -fr %{buildroot}%{_docdir}/%{name}

%files libs
%license COPYING.LIB
%doc CHANGES
%{_libdir}/lib%{name}.so.1
%{_libdir}/lib%{name}.so.1.3.0

%files cli
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz

%files gui
%{_bindir}/%{name}-gui
%{_datadir}/applications/%{name}-gui.desktop
%{_datadir}/applications/%{name}-gui-small.desktop
%{_datadir}/pixmaps/%{name}-gui.png
%{_datadir}/%{name}/
%{_mandir}/man1/%{name}-gui.1.gz

%files devel
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
