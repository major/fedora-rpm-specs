Name:           python-sphinx-inline-tabs
# There are 2 different versions here:
# https://github.com/pradyunsg/sphinx-inline-tabs/issues/7
Version:        2022.01.02~b11
%global tag     2022.01.02.beta11
Release:        5%{?dist}
Summary:        Add inline tabbed content to your Sphinx documentation
License:        MIT
URL:            https://github.com/pradyunsg/sphinx-inline-tabs
Source0:        %{url}/archive/%{tag}/sphinx-inline-tabs-%{tag}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%global _description %{expand:
Add inline tabbed content to your Sphinx documentation.

Features:

- Elegant design: Small footprint in the markup and generated website,
  while looking good.
- Configurable: All the colors can be configured using CSS variables.
- Synchronization: Tabs with the same label all switch with a single click.
- Works without JavaScript: JavaScript is not required for the basics, only for
  synchronization.}

%description %_description


%package -n python3-sphinx-inline-tabs
Summary:        %{summary}

%description -n python3-sphinx-inline-tabs  %_description


%prep
%autosetup -p1 -n sphinx-inline-tabs-%{tag}


%generate_buildrequires
# There is a [test] extra, but there are no tests :/
# https://github.com/pradyunsg/sphinx-inline-tabs/issues/6
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files sphinx_inline_tabs


%files -n python3-sphinx-inline-tabs -f %{pyproject_files}
%doc README.md
%doc CODE_OF_CONDUCT.md
%license LICENSE


%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2022.01.02~b11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2022.01.02~b11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2022.01.02~b11-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2022.01.02~b11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jan 07 2022 Malcolm Inglis <miinglis@amazon.com> - 2022.01.02~b11-1
- Update to upstream version
- Fixes: rhbz#1994751

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2021.04.11~b9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 23 2021 Karolina Surma <ksurma@redhat.com> - 2021.04.11~b9-1
- Update to upstream version
- Fixes: rhbz#1941094

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2020.10.19~b4-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020.10.19~b4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 30 2020 Miro Hrončok <mhroncok@redhat.com> - 2020.10.19~b4-1
- Initial package
- Fixes: rhbz#1902760
