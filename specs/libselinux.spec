%define ruby_inc %(pkg-config --cflags ruby)
%define libsepolver 3.8-0.rc3

Summary: SELinux library and simple utilities
Name: libselinux
Version: 3.8
Release: 0.rc3.1%{?dist}.2
License: LicenseRef-Fedora-Public-Domain
# https://github.com/SELinuxProject/selinux/wiki/Releases
Source0: https://github.com/SELinuxProject/selinux/releases/download/%{version}-rc3/libselinux-%{version}-rc3.tar.gz
Source1: https://github.com/SELinuxProject/selinux/releases/download/%{version}-rc3/libselinux-%{version}-rc3.tar.gz.asc
Source2: https://github.com/bachradsusi.gpg
Source3: selinuxconlist.8
Source4: selinuxdefcon.8

Url: https://github.com/SELinuxProject/selinux/wiki
# $ git clone https://github.com/fedora-selinux/selinux.git
# $ cd selinux
# $ git format-patch -N 3.8 -- libselinux
# $ i=1; for j in 00*patch; do printf "Patch%04d: %s\n" $i $j; i=$((i+1));done
# Patch list start
Patch0001: 0001-Use-SHA-2-instead-of-SHA-1.patch
# Patch list end
BuildRequires: gcc make
BuildRequires: ruby-devel ruby libsepol-static >= %{libsepolver} swig pcre2-devel
BuildRequires: python3 python3-devel python3-setuptools python3-wheel python3-pip
BuildRequires: systemd
BuildRequires: gnupg2
Requires: libsepol%{?_isa} >= %{libsepolver} pcre2
Conflicts: filesystem < 3, selinux-policy-base < 3.13.1-138

%description
Security-enhanced Linux is a feature of the Linux® kernel and a number
of utilities with enhanced security functionality designed to add
mandatory access controls to Linux.  The Security-enhanced Linux
kernel contains new architectural components originally developed to
improve the security of the Flask operating system. These
architectural components provide general support for the enforcement
of many kinds of mandatory access control policies, including those
based on the concepts of Type Enforcement®, Role-based Access
Control, and Multi-level Security.

libselinux provides an API for SELinux applications to get and set
process and file security contexts and to obtain security policy
decisions.  Required for any applications that use the SELinux API.

%package utils
Summary: SELinux libselinux utilities
Requires: %{name}%{?_isa} = %{version}-%{release}

%description utils
The libselinux-utils package contains the utilities

%package -n python3-libselinux
Summary: SELinux python 3 bindings for libselinux
Requires: %{name}%{?_isa} = %{version}-%{release}
%{?python_provide:%python_provide python3-libselinux}
# Remove before F30
Provides: %{name}-python3 = %{version}-%{release}
Provides: %{name}-python3%{?_isa} = %{version}-%{release}
Obsoletes: %{name}-python3 < %{version}-%{release}

%description -n python3-libselinux
The libselinux-python3 package contains python 3 bindings for developing
SELinux applications. 

%package ruby
Summary: SELinux ruby bindings for libselinux
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: ruby(selinux)

%description ruby
The libselinux-ruby package contains the ruby bindings for developing 
SELinux applications. 

%package devel
Summary: Header files and libraries used to build SELinux
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: libsepol-devel%{?_isa} >= %{libsepolver}

%description devel
The libselinux-devel package contains the libraries and header files
needed for developing SELinux applications. 

%package static
Summary: Static libraries used to build SELinux
Requires: %{name}-devel%{?_isa} = %{version}-%{release}

%description static
The libselinux-static package contains the static libraries
needed for developing SELinux applications. 

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p 2 -n libselinux-%{version}-rc3

%build
export DISABLE_RPM="y"
export USE_PCRE2="y"

%set_build_flags
CFLAGS="$CFLAGS -fno-semantic-interposition"

# To support building the Python wrapper against multiple Python runtimes
# Define a function, for how to perform a "build" of the python wrapper against
# a specific runtime:
BuildPythonWrapper() {
  BinaryName=$1

  # Perform the build from the upstream Makefile:
  %make_build \
    PYTHON=$BinaryName \
    LIBDIR="%{_libdir}" \
    pywrap
}

%make_build LIBDIR="%{_libdir}" swigify
%make_build LIBDIR="%{_libdir}" all

BuildPythonWrapper %{__python3}

%make_build RUBYINC="%{ruby_inc}" SHLIBDIR="%{_libdir}" LIBDIR="%{_libdir}" LIBSEPOLA="%{_libdir}/libsepol.a" rubywrap

%install
InstallPythonWrapper() {
  BinaryName=$1

  make \
    PYTHON=$BinaryName \
    DESTDIR="%{buildroot}" LIBDIR="%{_libdir}" \
    SHLIBDIR="%{_lib}" BINDIR="%{_bindir}" \
    SBINDIR="%{_sbindir}" \
    LIBSEPOLA="%{_libdir}/libsepol.a" \
    install-pywrap
}

rm -rf %{buildroot}
mkdir -p %{buildroot}%{_tmpfilesdir}
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_includedir}
mkdir -p %{buildroot}%{_sbindir}
install -d -m 0755 %{buildroot}%{_rundir}/setrans
echo "d %{_rundir}/setrans 0755 root root" > %{buildroot}%{_tmpfilesdir}/libselinux.conf

InstallPythonWrapper %{__python3}

%make_install LIBDIR="%{_libdir}" SHLIBDIR="%{_libdir}" BINDIR="%{_bindir}" SBINDIR="%{_sbindir}"
make DESTDIR="%{buildroot}" RUBYINSTALL=%{ruby_vendorarchdir} install-rubywrap

# Nuke the files we don't want to distribute
rm -f %{buildroot}%{_sbindir}/compute_*
rm -f %{buildroot}%{_sbindir}/deftype
rm -f %{buildroot}%{_sbindir}/execcon
rm -f %{buildroot}%{_sbindir}/getenforcemode
rm -f %{buildroot}%{_sbindir}/getfilecon
rm -f %{buildroot}%{_sbindir}/getpidcon
rm -f %{buildroot}%{_sbindir}/mkdircon
rm -f %{buildroot}%{_sbindir}/policyvers
rm -f %{buildroot}%{_sbindir}/setfilecon
rm -f %{buildroot}%{_sbindir}/selinuxconfig
rm -f %{buildroot}%{_sbindir}/selinuxdisable
rm -f %{buildroot}%{_sbindir}/getseuser
rm -f %{buildroot}%{_sbindir}/togglesebool
rm -f %{buildroot}%{_sbindir}/selinux_check_securetty_context
mv %{buildroot}%{_sbindir}/getdefaultcon %{buildroot}%{_sbindir}/selinuxdefcon
mv %{buildroot}%{_sbindir}/getconlist %{buildroot}%{_sbindir}/selinuxconlist
install -d %{buildroot}%{_mandir}/man8/
install -m 644 %{SOURCE3} %{buildroot}%{_mandir}/man8/
install -m 644 %{SOURCE4} %{buildroot}%{_mandir}/man8/
rm -f %{buildroot}%{_mandir}/man8/togglesebool*

%ldconfig_scriptlets

%files
%license LICENSE
%{_libdir}/libselinux.so.*
%dir %{_rundir}/setrans/
%{_tmpfilesdir}/libselinux.conf

%files utils
%{_sbindir}/avcstat
%{_sbindir}/getenforce
%{_sbindir}/getpidprevcon
%{_sbindir}/getpolicyload
%{_sbindir}/getsebool
%{_sbindir}/matchpathcon
%{_sbindir}/sefcontext_compile
%{_sbindir}/selinuxconlist
%{_sbindir}/selinuxdefcon
%{_sbindir}/selinuxexeccon
%{_sbindir}/selinuxenabled
%{_sbindir}/setenforce
%{_sbindir}/selabel_compare
%{_sbindir}/selabel_digest
%{_sbindir}/selabel_lookup
%{_sbindir}/selabel_lookup_best_match
%{_sbindir}/selabel_partial_match
%{_sbindir}/selinux_check_access
%{_sbindir}/selabel_get_digests_all_partial_matches
%{_sbindir}/validatetrans
%{_mandir}/man5/*
%{_mandir}/man8/*

%files devel
%{_libdir}/libselinux.so
%{_libdir}/pkgconfig/libselinux.pc
%{_includedir}/selinux/
%{_mandir}/man3/*

%files static
%{_libdir}/libselinux.a

%files -n python3-libselinux
%{python3_sitearch}/selinux/
%{python3_sitearch}/selinux-%{version}*
%{python3_sitearch}/_selinux*

%files ruby
%{ruby_vendorarchdir}/selinux.so

%changelog
* Sun Jan 12 2025 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.8-0.rc3.1.2
- Rebuilt for the bin-sbin merge (2nd attempt)

* Wed Jan 08 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.8-0.rc3.1.1
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.4


%autochangelog
