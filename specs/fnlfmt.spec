Name:           fnlfmt
Version:        0.3.2
Release:        %autorelease
Summary:        A formatter for Fennel code

# manpage says MIT/X11, asking upstream to clarify:
# https://lists.sr.ht/~technomancy/fennel/%3Caf68ef034a053ab1694a6a5030c5963662156c38.camel@michel-slm.name%3E
License:        MIT
URL:            https://fennel-lang.org/
Source:         https://git.sr.ht/~technomancy/fnlfmt/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  lua-devel >= 5.1
BuildRequires:  fennel
BuildRequires:  make

Provides:       lua-fnlfmt = %{version}-%{release}
Recommends:     fennel
Supplements:    fennel

%description
Format your Fennel!

The goal of `fnlfmt` is *not* to be The One Formatter that all Fennel
programmers use to format their code. We assume that most of the time,
Fennel programmers will use a text editor that already knows how to
indent code correctly, and that `fnlfmt` supplements existing editor
support in cases where for whatever reason the editor functionality
cannot be used. This means that `fnlfmt` should be treated as one
implementation of the standard format rather than being canonical itself.

By design there is no way to configure it. When it comes to
indentation, the choices it makes should be correct other than bugs or
when new features are added to Fennel itself. When it comes to where
the line breaks are inserted, it tries its best, but there are
certainly cases where a human could do better. Sometimes when it comes
to line breaks it will defer to the existing code where possible.


%prep
%autosetup -p1
# use the system Fennel
rm fennel


%build
%make_build \
    LUA=lua \
    FENNEL=%{_bindir}/fennel


%install
%make_install \
    LUA=lua \
    FENNEL=%{_bindir}/fennel \
    PREFIX=%{_prefix}


%check
make test \
     LUA=lua \
     FENNEL=%{_bindir}/fennel


%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{lua_pkgdir}/%{name}.lua
%{_mandir}/man1/%{name}.1*


%changelog
%autochangelog
