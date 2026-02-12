# This spec file has been automatically updated
%if 0%{?fedora}
%bcond_without mingw
%else
%bcond_with mingw
%endif


Version:        0.26.2
Release:        %{?autorelease}%{!?autorelease:1%{?dist}}
Name:           p11-kit
Summary:        Library for loading and sharing PKCS#11 modules

License:        BSD-3-Clause
URL:            http://p11-glue.freedesktop.org/p11-kit.html
Source0:        https://github.com/p11-glue/p11-kit/releases/download/%{version}/p11-kit-%{version}.tar.xz
Source1:        https://github.com/p11-glue/p11-kit/releases/download/%{version}/p11-kit-%{version}.tar.xz.sig
Source2:        https://p11-glue.github.io/p11-glue/p11-kit/p11-kit-release-keyring.gpg
Source3:        trust-extract-compat
Source4:        p11-kit-client.service

BuildRequires:  gcc
BuildRequires:  libtasn1-devel >= 2.3
BuildRequires:  libffi-devel
BuildRequires:  gettext
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  systemd-devel
BuildRequires:  pkgconfig(bash-completion)
# Work around for https://bugzilla.redhat.com/show_bug.cgi?id=1497147
# Remove this once it is fixed
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  gnupg2
BuildRequires:  /usr/bin/xsltproc

%if %{with mingw}
BuildRequires:  ninja-build

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-libffi
BuildRequires:  mingw32-libtasn1

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-libffi
BuildRequires:  mingw64-libtasn1
%endif


%description
p11-kit provides a way to load and enumerate PKCS#11 modules, as well
as a standard configuration setup for installing PKCS#11 modules in
such a way that they're discoverable.


%package client
Summary:        Client module from %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      %{name}-server < 0.25.5-8

%description client
The %{name}-client package contains a PKCS#11 module that enables
accessing other PKCS#11 modules over a Unix domain socket.  Note that
this feature is still experimental.


%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package trust
Summary:            System trust module from %{name}
Requires:           %{name}%{?_isa} = %{version}-%{release}
Requires(post):     %{_sbindir}/alternatives
Requires(postun):   %{_sbindir}/alternatives
Conflicts:          nss < 3.14.3-9

%description trust
The %{name}-trust package contains a system trust PKCS#11 module which
contains certificate anchors and blocklists.


%package server
Summary:        Server command for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      %{name}-server < 0.25.5-8

%description server
The %{name}-server package contains command line tools that enable to
export PKCS#11 modules through a Unix domain socket.  Note that this
feature is still experimental.


%if %{with mingw}
%package -n mingw32-%{name}
Summary:        MinGW Library for loading and sharing PKCS#11 modules
Requires:       pkgconfig
BuildArch:      noarch

%description -n mingw32-%{name}
p11-kit provides a way to load and enumerate PKCS#11 modules, as well as
a standard configuration setup for installing PKCS#11 modules in such a
way that they're discoverable.  This library is cross-compiled for MinGW.


%package -n mingw64-%{name}
Summary:        MinGW Library for loading and sharing PKCS#11 modules
Requires:       pkgconfig
BuildArch:      noarch

%description -n mingw64-%{name}
p11-kit provides a way to load and enumerate PKCS#11 modules, as well as
a standard configuration setup for installing PKCS#11 modules in such a
way that they're discoverable.  This library is cross-compiled for MinGW.


%{?mingw_debug_package}
%endif


# solution taken from icedtea-web.spec
%define multilib_arches ppc64 sparc64 x86_64 ppc64le
%ifarch %{multilib_arches}
%define alt_ckbi  libnssckbi.so.%{_arch}
%else
%define alt_ckbi  libnssckbi.so
%endif


%prep
gpgv2 --keyring %{SOURCE2} %{SOURCE1} %{SOURCE0}

%autosetup -p1

%build
# These paths are the source paths that come from the plan here:
# https://fedoraproject.org/wiki/Features/SharedSystemCertificates:SubTasks
%meson -Dgtk_doc=true -Dman=true -Dtrust_paths=%{_sysconfdir}/pki/ca-trust/source:%{_datadir}/pki/ca-trust-source
%meson_build

%if %{with mingw}
%mingw_meson -Dgtk_doc=false -Dman=false -Dnls=false -Dtrust_paths=%{_sysconfdir}/pki/ca-trust/source:%{_datadir}/pki/ca-trust-source -Dzsh_completion=disabled
%mingw_ninja
%endif

%install
%meson_install
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/pkcs11/modules
install -p -m 755 %{SOURCE3} $RPM_BUILD_ROOT%{_libexecdir}/p11-kit/
# Install the example conf with %%doc instead
mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}
mv $RPM_BUILD_ROOT%{_sysconfdir}/pkcs11/pkcs11.conf.example $RPM_BUILD_ROOT%{_docdir}/%{name}/pkcs11.conf.example
mkdir -p $RPM_BUILD_ROOT%{_userunitdir}
install -p -m 644 %{SOURCE4} $RPM_BUILD_ROOT%{_userunitdir}
%find_lang %{name}

%if %{with mingw}
%mingw_ninja_install

%{?mingw_debug_install_post}
%endif

%check
%meson_test


%post trust
alternatives --install %{_libdir}/libnssckbi.so %{alt_ckbi} %{_libdir}/pkcs11/p11-kit-trust.so 30

%postun trust
if [ $1 -eq 0 ] ; then
        # package removal
        alternatives --remove %{alt_ckbi} %{_libdir}/pkcs11/p11-kit-trust.so
fi


%files -f %{name}.lang
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc AUTHORS NEWS README
%{_docdir}/%{name}/pkcs11.conf.example
%dir %{_sysconfdir}/pkcs11
%dir %{_sysconfdir}/pkcs11/modules
%dir %{_datadir}/p11-kit
%dir %{_datadir}/p11-kit/modules
%dir %{_libdir}/pkcs11
%dir %{_libexecdir}/p11-kit
%{_bindir}/p11-kit
%{_libdir}/libp11-kit.so.*
%{_libdir}/p11-kit-proxy.so
%{_libexecdir}/p11-kit/p11-kit-remote
%{_mandir}/man1/trust.1.gz
%{_mandir}/man8/p11-kit.8.gz
%{_mandir}/man5/pkcs11.conf.5.gz
%{_datadir}/bash-completion/completions/p11-kit
%{_datadir}/zsh/site-functions/_p11-kit

%files client
%{_libdir}/pkcs11/p11-kit-client.so
%{_userunitdir}/p11-kit-client.service

%files devel
%{_includedir}/p11-kit-1/
%{_libdir}/libp11-kit.so
%{_libdir}/pkgconfig/p11-kit-1.pc
%doc %{_datadir}/gtk-doc/

%files trust
%{_bindir}/trust
%ghost %{_libdir}/libnssckbi.so
%{_libdir}/pkcs11/p11-kit-trust.so
%{_datadir}/p11-kit/modules/p11-kit-trust.module
%{_libexecdir}/p11-kit/trust-extract-compat
%{_datadir}/bash-completion/completions/trust
%{_datadir}/zsh/site-functions/_trust

%files server
%{_libexecdir}/p11-kit/p11-kit-server
%{_userunitdir}/p11-kit-server.service
%{_userunitdir}/p11-kit-server.socket

%if %{with mingw}
%files -n mingw32-%{name}
%{!?_licensedir:%global license %%doc}
%license COPYING
%{mingw32_bindir}/libp11-kit-0.dll
%{mingw32_bindir}/p11-kit.exe
%{mingw32_bindir}/trust.exe
%{mingw32_libdir}/libp11-kit.dll.a
%dir %{mingw32_libdir}/pkcs11/
%{mingw32_libdir}/pkcs11/p11-kit-trust.dll
%{mingw32_libdir}/pkcs11/p11-kit-trust.dll.a
%{mingw32_libdir}/pkgconfig/p11-kit-1.pc
%dir %{mingw32_libexecdir}/p11-kit/
%{mingw32_libexecdir}/p11-kit/*.exe
%{mingw32_libexecdir}/p11-kit/trust-extract-compat
%{mingw32_includedir}/p11-kit-1/
%{mingw32_datadir}/p11-kit/
%{mingw32_sysconfdir}/pkcs11/

%files -n mingw64-%{name}
%{!?_licensedir:%global license %%doc}
%license COPYING
%{mingw64_bindir}/libp11-kit-0.dll
%{mingw64_bindir}/p11-kit.exe
%{mingw64_bindir}/trust.exe
%{mingw64_libdir}/libp11-kit.dll.a
%dir %{mingw64_libdir}/pkcs11/
%{mingw64_libdir}/pkcs11/p11-kit-trust.dll
%{mingw64_libdir}/pkcs11/p11-kit-trust.dll.a
%{mingw64_libdir}/pkgconfig/p11-kit-1.pc
%dir %{mingw64_libexecdir}/p11-kit/
%{mingw64_libexecdir}/p11-kit/*.exe
%{mingw64_libexecdir}/p11-kit/trust-extract-compat
%{mingw64_includedir}/p11-kit-1/
%{mingw64_datadir}/p11-kit/
%{mingw64_sysconfdir}/pkcs11/
%endif


%changelog
%autochangelog
