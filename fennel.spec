Name:           fennel
Version:        1.3.0
Release:        %autorelease
Summary:        A Lisp that compiles to Lua

License:        MIT
URL:            https://fennel-lang.org/
Source0:        https://git.sr.ht/~technomancy/fennel/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  lua-devel >= 5.1
BuildRequires:  make

Provides:       lua-fennel = %{version}-%{release}
%if 0%{?rhel} && 0%{?rhel} < 9
%lua_requires
%endif
Recommends:     lua-readline

%description
Fennel is a Lisp that compiles to Lua. It aims to be easy to use, expressive,
and has almost zero overhead compared to handwritten Lua.

* *Full Lua compatibility* - You can use any function or library from Lua.
* *Zero overhead* - Compiled code should be just as or more efficient than
   hand-written Lua.
* *Compile-time macros* - Ship compiled code with no runtime dependency on
   Fennel.
* *Embeddable* - Fennel is a one-file library as well as an executable. Embed it
   in other programs to support runtime extensibility and interactive
   development.

At https://fennel-lang.org there's a live in-browser repl you can use without
installing anything.


%prep
%autosetup -p1


%build
%make_build


%install
%make_install \
  LUA_VERSION=%{lua_version} \
  MAN_DIR=%{_mandir}/man1 \
  PREFIX=%{_prefix}
MAN1=%{buildroot}%{_mandir}/man1/
mkdir -p ${MAN1}
cp -p fennel.1 ${MAN1}/


%check
make test


%files
%license LICENSE
%doc README.md CODE-OF-CONDUCT.md CONTRIBUTING.md
%doc api.md changelog.md lua-primer.md reference.md tutorial.md
%{_bindir}/fennel
%{lua_pkgdir}/fennel.lua
%{_mandir}/man1/fennel.1*


%changelog
%autochangelog
