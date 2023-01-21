%global sum Entity Relation Diagrams generation tool
%global desc \
ERAlchemy generates Entity Relation (ER) diagram (like the one below) from \
databases or from SQLAlchemy models.
%global srcname ERAlchemy

Name:           eralchemy
Version:        1.2.10
Release:        13%{?dist}
Summary:        %{sum}

License:        ASL 2.0
URL:            https://github.com/Alexis-benoist/eralchemy
Source0:        %pypi_source

BuildArch:      noarch

Requires:       python3-%name = %version-%release

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Patch:          ERAlchemy-1.2.10-compat-with-sqlalchemy-1.4.patch

%description
%desc


%package -n python3-%name
Summary:        %sum

%description -n python3-%name
%desc


%prep
%autosetup -p1 -n %srcname-%version


%build
%py3_build


%install
%py3_install


%check


%files
%doc readme.md
%_bindir/eralchemy


%files -n python3-%name
%python3_sitelib/ERAlchemy-%version-*.egg-info
%python3_sitelib/eralchemy/*.py
%python3_sitelib/eralchemy/__pycache__


%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.10-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.10-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.2.10-11
- Rebuilt for Python 3.11

* Tue Feb 01 2022 Pavel Raiskup <praiskup@redhat.com> - 1.2.10-10
- compat fix with new SQLAlchemy, per https://github.com/Alexis-benoist/eralchemy/issues/80

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.2.10-7
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2.10-4
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 17 2019 Pavel Raiskup <praiskup@redhat.com> - 1.2.10-2
- keep the %%_bindir script only in 'eralchemy' package (rhbz#1750263)

* Wed Sep 11 2019 Pavel Raiskup <praiskup@redhat.com> - 1.2.10-1
- apply review fixes (rhbz#1750263)

* Mon Sep 09 2019 Pavel Raiskup <praiskup@redhat.com> - 1.2.10-0
- initial RPM packaging
