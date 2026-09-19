Name:           antifennel
Version:        0.3.1
Release:        %autorelease
Summary:        Turn Lua code into Fennel code

License:        MIT
URL:            https://fennel-lang.org/
Source:         https://git.sr.ht/~technomancy/antifennel/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch:          antifennel-fix-expected-version.diff
Patch:          antifennel-skip-failing-test.patch
Patch:          antifennel-skip-irc-test.diff
Patch:          antifennel-fix-test-getinfo.diff

BuildArch:      noarch

BuildRequires:  lua-devel >= 5.1
BuildRequires:  make
BuildRequires:  pandoc

Provides:       lua-antifennel = %{version}-%{release}
Recommends:     fennel
Recommends:     lua-readline

%description
Turn Lua code into Fennel code. This compiler does the opposite of
what the Fennel compiler does.

There is a web-based demo at https://fennel-lang.org/see where you can
see it in action on Fennel's web site without installing anything.


%prep
%autosetup -p1


%build
%make_build LUA=lua


%install
%make_install \
  PREFIX=%{_prefix}


%check
make test LUA=lua


%files
%license LICENSE
%doc README.md
%{_bindir}/antifennel
%{_mandir}/man1/antifennel.1*


%changelog
%autochangelog
