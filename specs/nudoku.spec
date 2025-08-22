Name:           nudoku
Version:        6.0.0
Release:        %autorelease
Summary:        Ncurses based Sudoku game
License:        GPL-3.0-only
Url:            https://github.com/jubalh/%{name}
Source0:        https://github.com/jubalh/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cairo-devel
BuildRequires:  gettext-devel
BuildRequires:  ncurses-devel

%description
nudoku is a ncurses based Sudoku game.

%prep
%autosetup -p1

%build
autoreconf -i
export CFLAGS="%{build_cflags} -I%{_datadir}/gettext"
%configure --enable-cairo
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
%find_lang %{name}

%files -f %{name}.lang
%license LICENSE
%doc README.md
%{_bindir}/nudoku
%{_mandir}/man6/nudoku.6.*

%changelog
%autochangelog
