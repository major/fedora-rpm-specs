Name:           janet
Version:        1.41.1
Release:        %autorelease
Summary:        A dynamic language and bytecode vm

License:        MIT
URL:            https://janet-lang.org
Source0:        https://github.com/janet-lang/janet/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  meson

%description
Janet makes a good system scripting language, or a language
to embed in other programs. It's like Lua and GNU Guile in
that regard. It has more built-in functionality and a richer
core language than Lua, but smaller than GNU Guile or Python.
However, it is much easier to embed and port than Python or
Guile.

There is a REPL for trying out the language, as well as the
ability to run script files. This client program is separate
from the core runtime, so Janet can be embedded in other
programs. Try Janet in your browser at https://janet-lang.org.

%package devel
Summary:   A dynamic language and bytecode vm
Requires:  %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for Janet.


%prep
%autosetup -n %{name}-%{version}
rm examples/numarray/.gitignore

%build
%meson --buildtype=release -Ddefault_library=shared
%meson_build
# Create HTML documentation file
%{_vpath_builddir}/janet tools/gendoc.janet  > doc.html

%install
%meson_install
# Amalgamated janet.c file is used to embed Janet in C applications
mkdir -p %{buildroot}/%{_libdir}/janet
install -Dm644 %{_builddir}/%{name}-%{version}/%{_vpath_builddir}/janet.c \
 %{buildroot}/%{_libdir}/janet/janet.c
install -Dm644 src/conf/janetconf.h %{buildroot}/%{_includedir}/janetconf.h
# Do not package hidden file
rm %{buildroot}/%{_libdir}/janet/.keep

%check
%meson_test

%files
%license LICENSE
%doc README.md
%doc CHANGELOG.md
%doc doc.html
%doc examples/
%{_mandir}/man1/janet.1*
%{_bindir}/janet
%{_libdir}/libjanet.so.1.*

%files devel
%{_libdir}/pkgconfig/janet.pc
%{_includedir}/janet.h
%{_includedir}/janetconf.h
%{_libdir}/libjanet.so
%dir %{_includedir}/janet
%{_includedir}/janet/janet.h
%{_includedir}/janet/janet_%{version}.h
%dir %{_libdir}/janet
%{_libdir}/janet/janet.c

%changelog
%autochangelog
