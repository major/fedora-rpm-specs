%global forgeurl https://github.com/tsyrogit/zxcvbn-c
Version:        2.5
%forgemeta

Name:           zxcvbn-c
Release:        %autorelease
Summary:        C/C++ version of the zxcvbn password strength estimator
License:        MIT
URL:            %{forgeurl}
Source0:        %{forgesource}
Patch:          gcc15-c++23_fix.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc-c++


%description
This is a C/C++ implementation of the zxcvbn password strength estimation.
The code is intended to be included as part of the source of a C/C++ program.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}


%prep
%forgeautosetup


%build
%make_build


%install
# Make install is currently broken
#%%make_install

%{__mkdir_p} %{buildroot}%{_libdir}
%{__mkdir_p} %{buildroot}%{_bindir}
%{__mkdir_p} %{buildroot}{%{_includedir},%{_datadir}}/zxcvbn
install -p -m 0644 *.h %{buildroot}%{_includedir}/zxcvbn
cp -a libzxcvbn.so* %{buildroot}%{_libdir}
install -p -m 0755 dictgen %{buildroot}%{_bindir}
install -p -m 0644 zxcvbn.dict %{buildroot}%{_datadir}/zxcvbn


%check
make test


%files
%doc README.md
%license LICENSE.txt
%{_bindir}/dictgen
%{_libdir}/libzxcvbn.so.0*
%{_datadir}/zxcvbn


%files devel
%{_includedir}/zxcvbn
%{_libdir}/libzxcvbn.so


%changelog
%autochangelog
