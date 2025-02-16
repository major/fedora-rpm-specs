Version:        2.8.12

%global forgeurl https://github.com/cminyard/gensio
%forgemeta

# To keep dependencies at bay features that have heavier dependencies are split
# out into subpackages

Name:           gensio
Release:        %autorelease
Summary:        General Stream I/O

License:        GPL-2.0-only AND LGPL-2.1-only AND Apache-2.0
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  alsa-lib-devel
BuildRequires:  avahi-devel
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  OpenIPMI-devel
BuildRequires:  openssl-devel
BuildRequires:  pam-devel
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(libsctp)
BuildRequires:  python3-devel
BuildRequires:  swig
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  tcl-devel

%description
This is gensio (pronounced gen'-see-oh), a framework for giving a consistent
view of various stream (and packet) I/O types. You create a gensio object (or
a gensio), and you can use that gensio without having to know too much about
what is going on underneath. You can stack gensio on top of another one to add
protocol functionality. For instance, you can create a TCP gensio, stack SSL on
top of that, and stack Telnet on top of that. It supports a number of network
I/O and serial ports. gensios that stack on other gensios are called filters.

You can do the same thing with receiving ports. You can set up a gensio
accepter (accepter) to accept connections in a stack. So in our previous
example, you can setup TCP to listen on a specific port and automatically stack
SSL and Telnet on top when the connection comes in, and you are not informed
until everything is ready.

A very important feature of gensio is that it makes establishing encrypted and
authenticated connections much easier than without it. Beyond basic key
management, it's really no harder than TCP or anything else. It offers extended
flexibility for controlling the authentication process if needed. It's really
easy to use.

Note that the gensio(5) man page has more details on individual gensio types.


%package     -n libgensio
Summary:        Dynamic gensio Libraries
# Required as it installs and owns /run/lock/lockdev folder used for
# UUCP locking
Requires:       lockdev

%description -n libgensio
The %{name} package contains libraries for applications that use %{name}.


%package     -n libgensio-devel
Summary:        Development files for %{name}
Requires:       lib%{name}%{?_isa} = %{version}-%{release}

%description -n libgensio-devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package     -n libgensio-ipmisol
Summary:        OpenIPMI support for %{name}

%description -n libgensio-ipmisol
The %{name}-ipmisol package contains additional libraries for OpenIPMI
support in %{name}.


%package     -n libgensio-mdns
Summary:        Avahi (mDNS) support for %{name}

%description -n libgensio-mdns
The %{name}-mdns package contains additional libraries for Avahi (mDNS)
support in %{name}.


%package     -n libgensio-sound
Summary:        ALSA support for %{name}

%description -n libgensio-sound
The %{name}-sound package contains additional libraries for ALSA sound
support in %{name}.


%package     -n libgensio-tcl
Summary:        TCL bindings for %{name}

%description -n libgensio-tcl
The %{name}-tcl package contains TCL bindings for %{name}.


%package     -n python3-%{name}
Summary:        Python library for %{name}

%description -n python3-%{name}
The %{name}-python package contains Python bindings for %{name}.


%prep
%forgeautosetup -p1


%build
autoreconf -f -i
# Go bindings are available from https://github.com/cminyard/go, not building them here
%configure \
  --enable-static=no \
  --with-go=no \
  --with-pythoninstall=%{python3_sitearch} \
  --with-uucp-locking=%{_rundir}/lock/lockdev
# Fix linker bloat
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool

%make_build


%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
sed -i 's|/usr/local/sbin|%{sbindir}|g' tools/gtlsshd.service
install -Dpm 0644 tools/gtlsshd.service %{buildroot}/%{_unitdir}/gtlsshd.service


%post
%systemd_post gtlsshd.service

%preun
%systemd_preun gtlsshd.service

%postun
%systemd_postun_with_restart gtlsshd.service


%files
%license COPYING COPYING.LIB
%doc docs
%doc AUTHORS ChangeLog FAQ.rst NEWS README.rst SECURITY.md
%{_bindir}/%{name}t
%{_bindir}/gagwpe
%{_bindir}/gmdns
%{_bindir}/greflector
%{_bindir}/gsound
%{_bindir}/gtlssh
%{_bindir}/gtlssh-keygen
%{_bindir}/gtlssync
%{_sbindir}/gtlsshd
%{_mandir}/man1/%{name}t.1.gz
%{_mandir}/man1/gmdns.1.gz
%{_mandir}/man1/greflector.1.gz
%{_mandir}/man1/gsound.1.gz
%{_mandir}/man1/gtlssh-keygen.1.gz
%{_mandir}/man1/gtlssh.1.gz
%{_mandir}/man1/gtlssync.1.gz
%{_mandir}/man5/%{name}.5.gz
%{_mandir}/man5/ser%{name}.5.gz
%{_mandir}/man8/gtlsshd.8.gz
%{_unitdir}/gtlsshd.service


%files -n libgensio
%license COPYING COPYING.LIB
%doc AUTHORS ChangeLog FAQ.rst NEWS README.rst SECURITY.md
%{_libdir}/lib%{name}.so.*
%{_libdir}/lib%{name}cpp.so.*
%{_libdir}/lib%{name}glib.so.*
%{_libdir}/lib%{name}osh.so.*
%{_libdir}/lib%{name}oshcpp.so.*
%dir %{_libexecdir}/%{name}
%dir %{_libexecdir}/%{name}/%{version}
%{_libexecdir}/%{name}/%{version}/lib%{name}_afskmdm.so
%{_libexecdir}/%{name}/%{version}/lib%{name}_ax25.so
%{_libexecdir}/%{name}/%{version}/lib%{name}_certauth.so
%{_libexecdir}/%{name}/%{version}/lib%{name}_cm108gpio.so
%{_libexecdir}/%{name}/%{version}/lib%{name}_conacc.so
%{_libexecdir}/%{name}/%{version}/lib%{name}_dgram.so
%{_libexecdir}/%{name}/%{version}/lib%{name}_dummy.so
%{_libexecdir}/%{name}/%{version}/lib%{name}_echo.so
%{_libexecdir}/%{name}/%{version}/lib%{name}_file.so
%{_libexecdir}/%{name}/%{version}/lib%{name}_keepopen.so
%{_libexecdir}/%{name}/%{version}/lib%{name}_kiss.so
%{_libexecdir}/%{name}/%{version}/lib%{name}_msgdelim.so
%{_libexecdir}/%{name}/%{version}/lib%{name}_mux.so
%{_libexecdir}/%{name}/%{version}/lib%{name}_net.so
%{_libexecdir}/%{name}/%{version}/lib%{name}_perf.so
%{_libexecdir}/%{name}/%{version}/lib%{name}_pty.so
%{_libexecdir}/%{name}/%{version}/lib%{name}_ratelimit.so
%{_libexecdir}/%{name}/%{version}/lib%{name}_relpkt.so
%{_libexecdir}/%{name}/%{version}/lib%{name}_script.so
%{_libexecdir}/%{name}/%{version}/lib%{name}_sctp.so
%{_libexecdir}/%{name}/%{version}/lib%{name}_serialdev.so
%{_libexecdir}/%{name}/%{version}/lib%{name}_ssl.so
%{_libexecdir}/%{name}/%{version}/lib%{name}_stdio.so
%{_libexecdir}/%{name}/%{version}/lib%{name}_telnet.so
%{_libexecdir}/%{name}/%{version}/lib%{name}_trace.so
%{_libexecdir}/%{name}/%{version}/lib%{name}_xlt.so


%files -n libgensio-devel
%license COPYING COPYING.LIB examples/LICENSE.apache
%doc examples/*.{c,py}
%{_includedir}/%{name}
%{_libdir}/lib%{name}*.so
%{_libdir}/pkgconfig/lib%{name}*.pc
%{_mandir}/man3/%{name}*
%{_mandir}/man3/ser%{name}*
%{_mandir}/man3/str_to_%{name}.3.gz
%{_mandir}/man3/str_to_%{name}_accepter.3.gz
%{_mandir}/man3/str_to_%{name}_accepter_child.3.gz
%{_mandir}/man3/str_to_%{name}_child.3.gz


%files -n libgensio-ipmisol
%license COPYING COPYING.LIB
%{_libexecdir}/%{name}/%{version}/lib%{name}_ipmisol.so


%files -n libgensio-mdns
%license COPYING COPYING.LIB
%{_libdir}/lib%{name}mdns.so.*
%{_libdir}/lib%{name}mdnscpp.so.*
%{_libexecdir}/%{name}/%{version}/lib%{name}_mdns.so


%files -n libgensio-sound
%license COPYING COPYING.LIB
%{_libexecdir}/%{name}/%{version}/lib%{name}_sound.so


%files -n libgensio-tcl
%license COPYING COPYING.LIB
%{_libdir}/lib%{name}tcl.so.*


%files -n python3-%{name}
%license COPYING COPYING.LIB
%doc glib/c++/swig/pygensio/README.rst
%{_libdir}/lib%{name}_python_swig.so.*
%{python3_sitearch}/_%{name}*.so
%{python3_sitearch}/_py%{name}*.so
%pycached %{python3_sitearch}/%{name}*.py
%pycached %{python3_sitearch}/py%{name}*.py


%changelog
%autochangelog
