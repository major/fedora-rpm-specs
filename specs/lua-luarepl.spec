%global forgeurl https://github.com/hoelzro/lua-repl
%global tag %{version}

Name:      lua-luarepl
Version:   0.10
Release:   7%{?dist}
Summary:   REPL.lua - a reusable Lua REPL written in Lua
License:   MIT
URL:       %{forgeurl}

%forgemeta
Source:    %{forgesource}

BuildArch:     noarch
BuildRequires: lua-devel

# https://github.com/hoelzro/lua-repl#recommended-packages
Recommends:    lua-linenoise
# Enable filename_completion plugin
Suggests:      lua-filesystem


%description
REPL.lua has two uses:

  - An alternative to the standalone interpreter included with Lua, one that
    supports things like plugins, tab completion, and automatic insertion of
    `return` in front of expressions.

  - A REPL library you may embed in your application, to provide all of the
    niceties of the standalone interpreter included with Lua and then some.

Many software projects have made the choice to embed Lua in their projects to
allow their users some extra flexibility.  Some of these projects would also
like to provide a Lua REPL in their programs for debugging or rapid development.
Most Lua programmers are familiar with the standalone Lua interpreter as a
Lua REPL; however, it is bound to the command line. Until now, Lua programmers
would have to implement their own REPL from scratch if they wanted to include
one in their programs. This project aims to provide a REPL implemented in pure
Lua that almost any project can make use of.

This library also includes an example application (rep.lua), which serves as an
alternative to the standalone interpreter included with Lua. If the
lua-linenoise library is installed, it uses linenoise for history and
tab completion; otherwise, it tries to use rlwrap for basic line editing.
If you would like the arrow keys to work as expected rather than printing things
like `^[[A`, please install the lua-linenoise library or the rlwrap program.

%prep
%forgesetup

%build
# Nothing to do here

%install
install -dD %{buildroot}%{lua_pkgdir}
cp -av repl/ %{buildroot}%{lua_pkgdir}

install -dD %{buildroot}%{_bindir}
install -p -m 755 rep.lua %{buildroot}%{_bindir}/rep.lua

%check
# Missing dependency on lua-testmore, only smoke test for now

LUA_PATH="%{buildroot}%{lua_pkgdir}/?.lua;%{buildroot}%{lua_pkgdir}/?/init.lua" \
lua -e 'local repl = require "repl.console"
print(repl.VERSION)'

%files
%license COPYING
%doc README.md
%doc Changes
%{_bindir}/rep.lua
%{lua_pkgdir}/repl/

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 16 2022 Jonny Heggheim <hegjon@gmail.com> - 0.10-1
- Initial package
