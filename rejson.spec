Name:		rejson
Version:	1.0.2
Release:	10%{?dist}
Summary:	JSON data type for Redis

# Commit ID for latest goodform fix (not released)
# https://fedoraproject.org/wiki/Packaging:SourceURL "Commit Revision"
%global commit a775dc17a93ca31eca186815600aac9a14eef2ac
%global short_commit %(c=%{commit}; echo ${c:0:7})

License:	AGPLv3
URL:		https://github.com/goodform
Source0:	https://github.com/goodform/%{name}/archive/%{commit}/%{name}-%{version}-%{short_commit}.tar.gz

BuildRequires: make
BuildRequires:  gcc
BuildRequires:	redis-devel
BuildRequires:	python3
BuildRequires:	python3-rmtest >= 1
BuildRequires:  redis >= 4
Requires:	redis(modules_abi)%{?_isa} = %{redis_modules_abi}
Requires:	redis >= 4

%description
ReJSON is a Redis module that implements the JSON Data
Interchange Standard as a native data type.  It allows
storing, updating and fetching JSON values from Redis.

%prep
%setup -q

%build
%set_build_flags
%make_build LD="gcc"

%check
make PYTHON="python3" test

%install
mkdir -p %{buildroot}%{redis_modules_dir}
install -pDm755 src/%{name}.so %{buildroot}%{redis_modules_dir}/%{name}.so

%files
%license LICENSE
%doc README.md docs/*.md docs/images/*
%{redis_modules_dir}/%{name}.so

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 17 2020 Nathan Scott <nathans@redhat.com> - 1.0.2-5
- Update the upstream sources for gcc 10 fix (BZ 1799972)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Sep 14 2018 Nathan Scott <nathans@redhat.com> - 1.0.2-1
- Update dependencies for python3 and latest rmtest package.
- Update the upstream sources (https://github.com/goodform).

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Mar 18 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.0.1-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 03 2018 Nathan Scott <nathans@redhat.com> - 1.0.1-1
- Remove python installation assumptions.
- Update to latest upstream release.

* Mon Nov 27 2017 Nathan Scott <nathans@redhat.com> - 1.0.0-1
- Add runtime testing using python-rmtest package.
- Update to latest upstream release.

* Fri Nov 17 2017 Nathan Scott <nathans@redhat.com> - 0.99.1-2
- Updated to add license file, from package review.

* Wed Nov 15 2017 Nathan Scott <nathans@redhat.com> - 0.99.1-1
- Initial package.
