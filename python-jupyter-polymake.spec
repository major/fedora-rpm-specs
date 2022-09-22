# Upstream does not release tarballs.  Instead the code is copied directly
# into the polymake distribution.  Therefore, we check out the code from git.
%global commit  704994092647daca93ad18d6853a5540fceb3794
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global gitdate 20180129

Name:           python-jupyter-polymake
Version:        0.16
Release:        20.%{gitdate}.%{shortcommit}%{?dist}
Summary:        Jupyter kernel for polymake

License:        WTFPL
URL:            https://github.com/polymake/jupyter-polymake
Source0:        %{url}/archive/%{commit}/jupyter-polymake-%{shortcommit}.tar.gz

# Polymake is no longer available on 32-bit platforms
# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
BuildArch:      noarch
ExclusiveArch:  noarch aarch64 ppc64le s390x x86_64

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist ipykernel}
BuildRequires:  %{py3_dist ipython}
BuildRequires:  %{py3_dist jupymake}
BuildRequires:  %{py3_dist jupyter-client}
BuildRequires:  %{py3_dist pexpect}
BuildRequires:  %{py3_dist pip}
BuildRequires:  %{py3_dist wheel}

%global _description %{expand:
This package contains a Jupyter kernel for polymake.}

%description %_description

%package     -n python3-jupyter-polymake
Summary:        Jupyter kernel for polymake
Requires:       python-jupyter-filesystem
Requires:       %{py3_dist ipykernel}
Requires:       %{py3_dist ipython}
Requires:       %{py3_dist jupymake}
Requires:       %{py3_dist jupyter-client}
Requires:       %{py3_dist pexpect}

%description -n python3-jupyter-polymake %_description

%prep
%autosetup -n jupyter-polymake-%{commit}

%build
%pyproject_wheel

%install
%pyproject_install

# Move the jupyter kernel files to where we want them in Fedora
mkdir -p %{buildroot}%{_datadir}/jupyter/kernels/polymake
mv %{buildroot}%{python3_sitelib}/jupyter_kernel_polymake/resources/* \
   %{buildroot}%{_datadir}/jupyter/kernels/polymake
rmdir %{buildroot}%{python3_sitelib}/jupyter_kernel_polymake/resources

%check
%py3_check_import jupyter_kernel_polymake

%files -n python3-jupyter-polymake
%doc README.md
%{_datadir}/jupyter/kernels/polymake/
%{python3_sitelib}/jupyter_kernel_polymake*

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-20.20180129.7049940
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Jerry James <loganjerry@gmail.com> - 0.16-19.20180129.7049940
- Do not build on i386 due to unavailability of polymake

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 0.16-19.20180129.7049940
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-18.20180129.7049940
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-17.20180129.7049940
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.16-16.20180129.7049940
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-15.20180129.7049940
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-14.20180129.7049940
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.16-13.20180129.7049940
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-12.20180129.7049940
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 21 2019 Jerry James <loganjerry@gmail.com> - 0.16-11.20180129.7049940
- Extracted from the polymake SRPM into its own package
