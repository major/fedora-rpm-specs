Name:           bitwise
Version:        0.43
Release:        2%{?dist}
Summary:        Terminal based bit manipulator in ncurses

# The entire source code is GPL-3.0-or-later except for
# the shunting-yard code and its test which are BSD 2-Clause
License:        GPL-3.0-or-later AND BSD-2-Clause
URL:            https://github.com/mellowcandle/bitwise
Source0:        %{url}/releases/download/v%{version}/%{name}-v%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(cunit)

%description
Bitwise is multi base interactive calculator supporting dynamic base conversion
and bit manipulation. It's a handy tool for low level hackers, kernel
developers and device drivers developers.

%prep
%autosetup -n %{name}-v%{version}

%build
%configure
%make_build

%install
%make_install

%check
%make_build check

%files
%license COPYING
%doc README ChangeLog NEWS
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.43-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Apr 20 2022 Gustavo Costa <xfgusta@fedoraproject.org> - 0.43-1
- Initial package
