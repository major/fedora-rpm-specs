#%%global _default_patch_fuzz 2

%global bootstrap 1

%global shortversion 5.4.0
%global libver 11

Name:           chicken
Version:        %{shortversion}
Release:        %autorelease
Summary:        A practical and portable Scheme system

License:        BSD-3-Clause
URL:            http://call-cc.org
Source0:        http://code.call-cc.org/releases/%{shortversion}/%{name}-%{version}.tar.gz
Patch0:         make_cflags_work.patch
BuildRequires:  gcc
BuildRequires:  chrpath
Requires:       chicken-libs%{?_isa} = %{version}-%{release}

# Old docs subpackage, which is no longer a subpackage
Obsoletes:      chicken-doc < 4.8.0.5-3
Provides:       chicken-doc = %{version}-%{release}

%if 0%{?rhel}
BuildRequires:  net-tools
%else
BuildRequires:  hostname
%endif

%if %{bootstrap} == 0
BuildRequires:  chicken
%endif
BuildRequires: make

%package libs
Summary:        Chicken Scheme runtime library

%description libs
The Chicken Scheme runtime library, linked to by programs compiled with
Chicken.

%package static
Summary:	Static library for Chicken
Requires:	chicken%{?_isa} = %{version}-%{release}

%description static
The Chicken Scheme runtime library, as a static library for users
to link against

%description
CHICKEN is a compiler for the Scheme programming language.
CHICKEN produces portable, efficient C, supports almost all of the R5RS
Scheme language standard, and includes many enhancements and extensions.

%prep
%autosetup -n %{name}-%{version}

%build
%if %{bootstrap} == 0

# This removes all C code from the repo, and leaves us only with Scheme code.
# Otherwise, it will try to compile C, defeating the point of bootstrapping.
make PLATFORM=linux spotless

# The above command nukes a necessary buildtag file, and there's no way that
# I can find to regenerate it - so instead we just generate it ourselves.
echo "#define C_BUILD_TAG \"compiled $(date '+%Y-%m-%d') on $(hostname)\"" > buildtag.h

%endif

# Chicken's build system is freaking horrible.
# So, Fedora requires that we use optflags here - makes sense, they contain
# some security related flags, etc. The issue is that Chicken uses the same
# flags that it was compiled with when it compiles code for the end-user.
# So if we pass -Wall here, it'll give the user a bunch of warnings when they
# compile anything at all with `csc`. So that's lovely. -codeblock

# Can't even use %%{make_build} or anything, since everything breaks... -sham1
make CFLAGS="$(echo "%{optflags}" | sed 's/-Wall//') -Wformat" \
     PREFIX=%{_prefix} \
     BINDIR=%{_bindir} \
     LIBDIR=%{_libdir} \
     DATADIR=%{_datadir}/chicken \
     INCLUDEDIR=%{_includedir} \
     INFODIR=%{_infodir}/chicken \
     TOPMANDIR=%{_mandir} \
     DOCDIR=%{_docdir}/chicken \
     PLATFORM=linux

%install
make CFLAGS="$(echo "%{optflags}" | sed 's/-Wall//') -Wformat" \
     PREFIX=%{_prefix} \
     BINDIR=%{_bindir} \
     LIBDIR=%{_libdir} \
     DATADIR=%{_datadir}/chicken \
     INCLUDEDIR=%{_includedir} \
     INFODIR=%{_infodir}/chicken \
     TOPMANDIR=%{_mandir} \
     DOCDIR=%{_docdir}/chicken \
     DESTDIR=%{buildroot} \
     PLATFORM=linux install

rm -f %{buildroot}/%{_docdir}/%{name}/LICENSE %{buildroot}/%{_docdir}/%{name}/README

find %{buildroot} -name \*.so -exec chrpath --delete \{\} \;
chrpath --delete %{buildroot}/%{_bindir}/chicken*
chrpath --delete %{buildroot}/%{_bindir}/csc
chrpath --delete %{buildroot}/%{_bindir}/csi

%check
make PLATFORM=linux check

%ldconfig_scriptlets libs

%files
%doc README
%license LICENSE
%dir %{_datadir}/chicken
%{_datadir}/chicken/setup.defaults
%{_bindir}/chicken*
%{_bindir}/csc
%{_bindir}/csi
%{_bindir}/feathers
%dir %{_includedir}/chicken
%{_includedir}/chicken/chicken-config.h
%{_includedir}/chicken/chicken.h
%{_datarootdir}/chicken/feathers.tcl
%dir %{_libdir}/chicken
%dir %{_libdir}/chicken/%{libver}
%{_libdir}/chicken/%{libver}/*
%{_mandir}/man1/*
%{_docdir}/chicken

%files libs
%{_libdir}/libchicken.so*

%files static
%{_libdir}/libchicken.a

%changelog
%autochangelog
