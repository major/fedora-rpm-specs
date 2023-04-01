Name:           qbe
Version:        1.1
Release:        %autorelease
Summary:        A pure C embeddable compiler backend

License:        MIT
URL:            https://c9x.me/compile/

Source0:        %{url}/release/%{name}-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  make

ExclusiveArch: x86_64 aarch64

%description
QBE is a compiler backend that aims to provide 70% of the performance of
industrial optimizing compilers in 10% of the code. QBE fosters language
innovation by offering a compact user-friendly and performant backend. The size
limit constrains QBE to focus on the essential and prevents embarking on a
never-ending path of diminishing returns.

%prep
%autosetup

%build
make CFLAGS="$CFLAGS -std=c11 -fPIE" %{?_smp_mflags}

%install
%make_install PREFIX=%{_prefix}
mkdir -p %{buildroot}/%{_docdir}/%{name}
cp -r -p doc/ %{buildroot}/%{_docdir}/%{name}

%check
make check

%files
%doc README
%license LICENSE
%{_bindir}/%{name}
%{_docdir}/%{name}/*

%changelog
%autochangelog
