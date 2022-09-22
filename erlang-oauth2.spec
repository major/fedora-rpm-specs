%global srcname oauth2


Name:       erlang-%{srcname}
Version:    0.7.0
Release:    8%{?dist}
BuildArch:  noarch
License:    MIT
Summary:    An Oauth2 implementation for Erlang
URL:        https://github.com/kivra/%{srcname}
Source0:    https://github.com/kivra/%{srcname}/archive/%{version}.tar.gz
Patch1:     erlang-oauth2-0001-Don-t-use-deprecated-funs-in-Erlang-18.patch
Patch2:     erlang-oauth2-0002-Pass-on-error-from-authenticate_user.patch
BuildRequires: erlang-meck
BuildRequires: erlang-proper
BuildRequires: erlang-rebar


%description
This library is designed to simplify the implementation of the server side of
OAuth2.


%prep
%autosetup -n %{srcname}-%{version} -p 1


%build
%{erlang_compile}


%install
%{erlang_install}


%check
%{erlang_test}


%files
%license LICENSE
%doc README.md
%{erlang_appdir}/


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 22 2019 Peter Lemenkov <lemenkov@gmail.com> - 0.7.0-1
- Update to 0.7.0.
- Switch to noarch.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Sep  9 2016 Peter Lemenkov <lemenkov@gmail.com> - 0.6.1-3
- Spec-file cleanups accorging to Fedora Erlang Packaging Guidelines

* Fri Mar 11 2016 Randy Barlow <rbarlow@redhat.com> - 0.6.1-2
- Rebuild to use the new automatic provides/requires build feature.

* Tue Feb 16 2016 Randy Barlow <rbarlow@redhat.com> - 0.6.1-1
- Update to 0.6.1.
- Re-enable tests on i686.
- Remove patch for Erlang 18 since it is fixed in this version.

* Sun Feb 07 2016 Randy Barlow <rbarlow@redhat.com> - 0.6.0-4
- Added a patch from upstream commit f1e0cb05 to fix support for Erlang 18.

* Sat Jan 09 2016 Randy Barlow <rbarlow@redhat.com> - 0.6.0-3
- Do not run the tests on i686.
- Use the Erlang macros more effectively.

* Tue Jan 05 2016 Randy Barlow <rbarlow@redhat.com> - 0.6.0-2
- Remove the noarch target, as it causes the package to install outside the erts path.
- Add a Requires on erlang-erts.

* Sun Dec 27 2015 Randy Barlow <rbarlow@redhat.com> - 0.6.0-1
- Initial release.
