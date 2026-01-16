Name:           fennel
Version:        1.6.1
Release:        %autorelease
Summary:        A Lisp that compiles to Lua

License:        MIT
URL:            https://fennel-lang.org/
Source:         https://git.sr.ht/~technomancy/fennel/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

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
  PREFIX=%{_prefix}


%check
make test


%files
%license LICENSE
%doc README.md CODE-OF-CONDUCT.md CONTRIBUTING.md
%doc api.md changelog.md lua-primer.md reference.md tutorial.md
%{_bindir}/fennel
%{lua_pkgdir}/fennel.lua
%{_mandir}/man1/fennel.1*
%{_mandir}/man3/fennel-api.3.gz
%{_mandir}/man5/fennel-reference.5.gz
%{_mandir}/man7/fennel-tutorial.7.gz


%changelog
%autochangelog
