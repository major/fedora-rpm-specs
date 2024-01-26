%global realname mozjs
%global upstream erlang-mozjs


Name:		erlang-js
Version:	1.9.3
Release:	6%{?dist}
Summary:	A Friendly Erlang to Javascript Binding
License:	ASL 2.0
URL:		http://github.com/%{upstream}/erlang-%{realname}
VCS:		scm:git:https://github.com/%{upstream}/erlang-%{realname}.git
Source0:	https://github.com/%{upstream}/erlang-%{realname}/archive/%{version}/erlang-%{realname}-%{version}.tar.gz
# https://github.com/erlang-mozjs/erlang-mozjs/pull/8
Patch01:    0001-Switch-default-mozjs-to-mozjs102.patch

BuildRequires:	erlang-mochiweb
BuildRequires:	erlang-rebar
BuildRequires:	gcc-c++
BuildRequires:	mozjs102-devel


%description
A Friendly Erlang to Javascript Binding.


%prep
%autosetup -p1 -n erlang-%{realname}-%{version}


%build
%{erlang_compile}


%install
%{erlang_install}
install -m 644 priv/json2.js $RPM_BUILD_ROOT%{_libdir}/erlang/lib/%{realname}-%{version}/priv


%check
# FIXME FIXME FIXME
# Fails with "too much recursion" on s390x, and I don't have access to any s390x machines
# Tracking bug - https://github.com/erlang-mozjs/erlang-mozjs/issues/1
# FIXME FIXME FIXME also strange issues on armv7hl, aarch64 (on armv7hl also
# but nobody cares anymore)
%ifnarch s390x aarch64
%{erlang_test}
%endif


%files
%license LICENSE
%doc README.org
%{erlang_appdir}/


%changelog
* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

%autochangelog
