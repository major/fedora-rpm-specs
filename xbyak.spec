Summary:        A C++ JIT assembler for x86
Name:           xbyak
License:        BSD-3-Clause

Version:        6.63
Release:        3%{?dist}

URL:            https://github.com/herumi/xbyak
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
# exception testing of allocator gets hung up on glibc double free check
Patch0:         xbyak-disable-noexecption-test3.patch

Group:          Development/Libraries
BuildArch:      noarch
ExclusiveArch:  x86_64

BuildRequires:  make
BuildRequires:  sed

%bcond_with check
%if %{with check}
# check
BuildRequires:  g++
#  -m32
BuildRequires:  glibc-devel(x86-32), libstdc++(x86-32)
BuildRequires:  nasm, yasm
%endif

%description
Xbyak is a C++ header library that enables dynamically to
assemble x86(IA32), x64(AMD64, x86-64) mnemonic.

The pronunciation of Xbyak is kəi-bja-k, かいびゃく.
It is named from a Japanese word 開闢, which means the beginning
of the world.

%package devel
Summary:        A C++ JIT assembler for x86
Provides:       xbyak-static = %{version}-%{release}

%description devel
Xbyak is a C++ header library that enables dynamically to
assemble x86(IA32), x64(AMD64, x86-64) mnemonic.

The pronunciation of Xbyak is kəi-bja-k, かいびゃく.
It is named from a Japanese word 開闢, which means the beginning
of the world.

%prep
%setup -q
%patch0 -p1

%build
# nothing to build

%install
mkdir -p %{buildroot}%{_datadir}/xbyak
cp COPYRIGHT %{buildroot}%{_datadir}/xbyak/
cp readme.* %{buildroot}%{_datadir}/xbyak/
cp doc/*.md %{buildroot}%{_datadir}/xbyak/
# fix dos lines
sed -i 's/\r$//' %{buildroot}%{_datadir}/xbyak/readme.txt
cp -r sample %{buildroot}%{_datadir}/xbyak/

%make_install PREFIX=%{buildroot}/usr

%if %{with check}
%check
make test
%endif

%files devel
%dir %{_datadir}/xbyak
%dir %{_includedir}/xbyak
%license %{_datadir}/xbyak/COPYRIGHT
%doc %{_datadir}/xbyak/readme.txt
%doc %{_datadir}/xbyak/*.md
%{_datadir}/xbyak/sample/
%{_includedir}/xbyak/*.h

%changelog
* Thu Oct 27 2022 Tom Rix <trix@redhat.com> - 6.63-3
- Make check optional

* Mon Oct 24 2022 Tom Rix <trix@redhat.com> - 6.63-2
- Add tests, samples
- Change license to BSD-3-Clause
- Check directory ownership
- Package as static library

* Fri Oct 21 2022 Tom Rix <trix@redhat.com> - 6.63-1
- Initial release
