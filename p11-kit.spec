# This spec file has been automatically updated
Version:        0.25.3
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
Patch:          p11-kit-0.25.3-import-object.patch

BuildRequires:  gcc
BuildRequires:  libtasn1-devel >= 2.3
BuildRequires:  libffi-devel
BuildRequires:  gettext
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  systemd-devel
BuildRequires:  bash-completion
# Work around for https://bugzilla.redhat.com/show_bug.cgi?id=1497147
# Remove this once it is fixed
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  gnupg2
BuildRequires:  /usr/bin/xsltproc

%description
p11-kit provides a way to load and enumerate PKCS#11 modules, as well
as a standard configuration setup for installing PKCS#11 modules in
such a way that they're discoverable.


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
Summary:        Server and client commands for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description server
The %{name}-server package contains command line tools that enable to
export PKCS#11 modules through a Unix domain socket.  Note that this
feature is still experimental.


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
# These paths are the source paths that  come from the plan here:
# https://fedoraproject.org/wiki/Features/SharedSystemCertificates:SubTasks
%meson -Dgtk_doc=true -Dman=true -Dtrust_paths=%{_sysconfdir}/pki/ca-trust/source:%{_datadir}/pki/ca-trust-source
%meson_build

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

%check
%meson_test


%post trust
%{_sbindir}/alternatives --install %{_libdir}/libnssckbi.so %{alt_ckbi} %{_libdir}/pkcs11/p11-kit-trust.so 30

%postun trust
if [ $1 -eq 0 ] ; then
        # package removal
        %{_sbindir}/alternatives --remove %{alt_ckbi} %{_libdir}/pkcs11/p11-kit-trust.so
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
%dir %{_libexecdir}/p11-kit
%{_bindir}/p11-kit
%{_libdir}/libp11-kit.so.*
%{_libdir}/p11-kit-proxy.so
%{_libexecdir}/p11-kit/p11-kit-remote
%{_mandir}/man1/trust.1.gz
%{_mandir}/man8/p11-kit.8.gz
%{_mandir}/man5/pkcs11.conf.5.gz
%{_datadir}/bash-completion/completions/p11-kit

%files devel
%{_includedir}/p11-kit-1/
%{_libdir}/libp11-kit.so
%{_libdir}/pkgconfig/p11-kit-1.pc
%doc %{_datadir}/gtk-doc/

%files trust
%{_bindir}/trust
%dir %{_libdir}/pkcs11
%ghost %{_libdir}/libnssckbi.so
%{_libdir}/pkcs11/p11-kit-trust.so
%{_datadir}/p11-kit/modules/p11-kit-trust.module
%{_libexecdir}/p11-kit/trust-extract-compat
%{_datadir}/bash-completion/completions/trust

%files server
%{_libdir}/pkcs11/p11-kit-client.so
%{_userunitdir}/p11-kit-client.service
%{_libexecdir}/p11-kit/p11-kit-server
%{_userunitdir}/p11-kit-server.service
%{_userunitdir}/p11-kit-server.socket


%changelog
%autochangelog
