Name:           ffcall
Version:        2.5
Release:        %autorelease
Summary:        Libraries for foreign function call interfaces

License:        GPL-2.0-or-later
URL:            https://www.gnu.org/software/libffcall/
VCS:            git:https://git.savannah.gnu.org/git/libffcall.git
Source:         https://ftp.gnu.org/gnu/libffcall/lib%{name}-%{version}.tar.gz
Patch:          configure.patch
# Update powerpc64 callback function.  Fixes clisp FTBFS.
Patch:          %{name}-ppc64le.patch

BuildRequires:  gcc
BuildRequires:  gnulib-devel
BuildRequires:  make

%description
This is a collection of four libraries which can be used to build
foreign function call interfaces in embedded interpreters.  The four
packages are:
 - avcall: calling C functions with variable arguments
 - vacall: C functions accepting variable argument prototypes
 - trampoline: closures as first-class C functions
 - callback: closures with variable arguments as first-class C functions
   (a reentrant combination of vacall and trampoline)

%package devel
Summary:        Files needed to develop programs with %{name}
# The project as a whole is GPL-2.0-or-later.
# The man pages and HTML documentation are GPL-2.0-or-later OR
# GFDL-1.2-no-invariants-or-later.
License:        GPL-2.0-or-later AND (GPL-2.0-or-later OR GFDL-1.2-no-invariants-or-later)
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Files needed to develop programs with %{name}.

%package static
Summary:        Static libraries for foreign function call interfaces
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description static
Static libraries for foreign function call interfaces.

%prep
%autosetup -n lib%{name}-%{version} -p1

%build
%configure

# Build the actual library
make # %{?_smp_mflags}

%install
mkdir -p $RPM_BUILD_ROOT%{_libdir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}
%make_install
rm -fr $RPM_BUILD_ROOT%{_datadir}/html
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

# Fix permissions
chmod a+x $RPM_BUILD_ROOT%{_libdir}/lib*.so.*

# Fix man pages with overly generic names (bz 800360)
pushd $RPM_BUILD_ROOT%{_mandir}/man3
for page in *; do
  mv $page %{name}-$page
done
popd

%files
%license COPYING
%doc README NEWS
%{_libdir}/libavcall.so.1*
%{_libdir}/libcallback.so.1*
%{_libdir}/libffcall.so.0*
%{_libdir}/libtrampoline.so.1*

%files devel
%doc avcall/avcall.html
%doc callback/callback.html
%doc callback/trampoline_r/trampoline_r.html
%doc trampoline/trampoline.html
%doc vacall/vacall.html
%{_includedir}/avcall.h
%{_includedir}/callback.h
%{_includedir}/ffcall*.h
%{_includedir}/trampoline.h
%{_includedir}/vacall*.h
%{_libdir}/libavcall.so
%{_libdir}/libcallback.so
%{_libdir}/libffcall.so
%{_libdir}/libtrampoline.so
%{_mandir}/man3/ffcall*

%files static
%{_libdir}/*.a

%changelog
%autochangelog
