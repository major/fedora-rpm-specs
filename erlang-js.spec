%global realname mozjs
%global upstream erlang-mozjs


Name:		erlang-js
Version:	1.9.3
Release:	2%{?dist}
Summary:	A Friendly Erlang to Javascript Binding
License:	ASL 2.0
URL:		http://github.com/%{upstream}/erlang-%{realname}
VCS:		scm:git:https://github.com/%{upstream}/erlang-%{realname}.git
Source0:	https://github.com/%{upstream}/erlang-%{realname}/archive/%{version}/erlang-%{realname}-%{version}.tar.gz
BuildRequires:	erlang-mochiweb
BuildRequires:	erlang-rebar
BuildRequires:	gcc-c++
BuildRequires:	mozjs91-devel


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
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

%autochangelog
