%if %{defined el9}
%global debug_package %{nil}
%endif

%global chez_version %(%{_bindir}/scheme --version 2>/dev/null || echo unknown)

# always bootstrap: otherwise rebuild fails
%bcond scm_boot 1

%bcond docs 1

# requires network?
%bcond test 0

# ppc64le s390x i686 give linking error with chez-scheme:
# - Exception: (while loading libc.so) /lib/libc.so: invalid ELF header
%ifarch ppc64le %{ix86}
# build with racket instead of chez-scheme
%bcond racket 1
%else
%bcond racket 0
%endif

%if %{with racket}
# /usr/lib/.build-id file for bin/idris2 conflicts with racket-minimal starter
%define _build_id_links alldebug
%endif

Name:           idris2
Version:        0.8.0
Release:        %autorelease
Summary:        Purely functional programming language with first class types

License:        BSD-3-Clause
URL:            https://www.idris-lang.org
Source0:        https://github.com/idris-lang/Idris2/archive/v%{version}/%{name}-%{version}.tar.gz

# i686: idris_signal.c:21:1: error: static assertion failed: "when not lock free, atomic functions are not async-signal-safe"
# ppc64le & s390x: Exception: (while loading libc.so) /lib64/libc.so: invalid ELF header
# ppc64le with Racket: extremely slow with portable bytecode vm
ExcludeArch:    ppc64le s390x %{ix86}
BuildRequires:  gcc
BuildRequires:  gmp-devel
BuildRequires:  make
%if %{without scm_boot}
BuildRequires:  idris2
%endif
%if %{with docs}
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
%endif
%if %{with test}
BuildRequires:  clang
%endif
%if %{with racket}
BuildRequires:  racket-minimal
BuildRequires:  racket-pkgs
Requires:       racket-minimal%{?_isa}
%else
# for scheme --version to stdout
BuildRequires:  chez-scheme >= 10.2
Requires:       chez-scheme%{?_isa} = %{chez_version}
%endif
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Provides:       %{name}-static = %{version}-%{release}
Recommends:     rlwrap

%description
Idris is a programming language designed to encourage Type-Driven Development.


%if %{with docs}
%package doc
Summary:        Idris2 documentation
%if %{defined fedora}
Requires:       fontawesome4-fonts
%else
Requires:       fontawesome-fonts
%endif
BuildArch:      noarch

%description doc
The package contains the idris2 manual
%endif


%package libs
Summary:        idris2 runtime support library
Obsoletes:      %{name}-lib < %{version}-%{release}

%description libs
The package provide the runtime support library for idris2.


%prep
%setup -q -n Idris2-%{version}


%build
%if %{with scm_boot}
make %{?with_racket:bootstrap-racket}%{!?with_racket:bootstrap SCHEME=scheme} PREFIX=%{_libdir}
%else
make
%endif

%if %{with docs}
make -C docs html
%endif


%install
export PATH=%{buildroot}/bin:$PATH
make install DESTDIR=%{buildroot} PREFIX=%{_libdir}

mkdir %{buildroot}%{_bindir}
%if %{without racket}
mv %{buildroot}%{_libdir}/bin/idris2_app/idris2.so %{buildroot}%{_bindir}/idris2
%else
mv %{buildroot}%{_libdir}/bin/idris2_app/idris2 %{buildroot}%{_bindir}/
%endif
rm %{buildroot}%{_libdir}/bin/idris2_app/libidris2_support.so

mv %{buildroot}%{_libdir}/%{name}-%{version}/lib/libidris2_support.so %{buildroot}%{_libdir}

mkdir -p %{buildroot}%{_datadir}/bash-completion/completions/
LD_LIBRARY_PATH="%{buildroot}%{_libdir}:" %{buildroot}%{_bindir}/idris2 --bash-completion-script %{name} | sed "s/dirnames/default/" > %{buildroot}%{_datadir}/bash-completion/completions/%{name}


%if %{with test}
%check
make test
%endif


# /usr/lib64/idris2-version/support/refc/libidris2_refc.a provides C backend runtime

%files
%doc *.md
%doc www/source/index.md
%{_bindir}/idris2
%{_libdir}/%{name}-%{version}
%{_datadir}/bash-completion/completions/%{name}
%exclude %{_libdir}/bin
%exclude %{_libdir}/%{name}-%{version}/lib


%if %{with docs}
%files doc
%doc docs/build/html
%endif


%files libs
%license LICENSE
%{_libdir}/libidris2_support.so


%changelog
%autochangelog
