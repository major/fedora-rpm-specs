Name:           python-mergedeep
Version:        1.3.4
Release:        15%{?dist}
Summary:        A deep merge function for python
BuildArch:      noarch

License:        MIT
URL:            https://github.com/clarketm/mergedeep
Source0:        https://github.com/clarketm/mergedeep/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  python3-devel

%description
A deep merge function for python.


%package -n python3-mergedeep
Summary:        %{summary}

%description -n python3-mergedeep
A deep merge function for python.


%prep
%autosetup -p1 -n mergedeep-%{version}


%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files mergedeep


%check
%tox


%files -n python3-mergedeep -f %{pyproject_files}
%doc README.md
%license LICENSE


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.3.4-13
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 1.3.4-9
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.3.4-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Sep 08 2021 Sandro Mani <manisandro@gmail.com> - 1.3.4-4
- Use %%pyproject_buildrequires -t

* Fri Sep 03 2021 Sandro Mani <manisandro@gmail.com> - 1.3.4-3
- Run %%tox in %%check

* Thu Sep 02 2021 Sandro Mani <manisandro@gmail.com> - 1.3.4-2
- Port to new Python guidelines

* Wed Sep 01 2021 Sandro Mani <manisandro@gmail.com> - 1.3.4-1
- Initial package
