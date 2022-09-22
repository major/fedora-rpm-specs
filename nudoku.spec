Name:           nudoku
Version:        2.1.0
Release:        %autorelease
Summary:        Ncurses based Sudoku game
License:        GPLv3
Url:            https://github.com/jubalh/%{name}
Source0:        https://github.com/jubalh/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

# Backport of https://github.com/jubalh/nudoku/commit/93899a0fd72e04b9f257e5f54af53466106b5959
Patch0:         0001-fix-for-ncurses-6_3.patch

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
