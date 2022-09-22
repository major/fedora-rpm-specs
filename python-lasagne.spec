%global modname lasagne
%global srcname Lasagne

# To have all examples/licenses/etc. in one directory
%global _docdir_fmt %{name}

Name:           python-%{modname}
Version:        0.1
Release:        24%{?dist}
Summary:        Lightweight library to build and train neural networks in Theano

License:        MIT
URL:            https://github.com/Lasagne/%{srcname}
Source0:        %{url}/archive/v%{version}/%{modname}-%{version}.tar.gz

BuildArch:      noarch

%description
Lasagne is a lightweight library to build and train neural networks in Theano.
Its main features are:

Supports feed-forward networks such as Convolutional Neural Networks (CNNs),
recurrent networks including Long Short-Term Memory (LSTM), and any combination
thereof
Allows architectures of multiple inputs and multiple outputs, including
auxiliary classifiers
Many optimization methods including Nesterov momentum, RMSprop and ADAM
Freely definable cost function and no need to derive gradients due to Theano's
symbolic differentiation
Transparent support of CPUs and GPUs due to Theano's expression compiler

%package -n python3-%{modname}
Summary:        Lightweight library to build and train neural networks in Theano
%{?python_provide:%python_provide python3-%{modname}}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       python3-theano

%description -n python3-%{modname}
Lasagne is a lightweight library to build and train neural networks in Theano.
Its main features are:

Supports feed-forward networks such as Convolutional Neural Networks (CNNs),
recurrent networks including Long Short-Term Memory (LSTM), and any combination
thereof
Allows architectures of multiple inputs and multiple outputs, including
auxiliary classifiers
Many optimization methods including Nesterov momentum, RMSprop and ADAM
Freely definable cost function and no need to derive gradients due to Theano's
symbolic differentiation
Transparent support of CPUs and GPUs due to Theano's expression compiler

This package allows for use of python-lasagne with Python 3.

%prep
%autosetup -n %{srcname}-%{version}
iconv --from-code UTF-8 --to-code US-ASCII -c CHANGES.rst > CHANGES
mv CHANGES CHANGES.rst
chmod -x examples/*
sed -i -e '1{\@^#!/usr/bin/env python@d}' examples/*.py

%build
%py3_build

%install
%py3_install

%check
# Tests requiring CUDA or pylearn2. Those are not packaged
#%{__python3} setup.py test

%files -n python3-%{modname}
%license LICENSE
%doc docs/ examples/ CHANGES.rst
%{python3_sitelib}/%{modname}/
%{python3_sitelib}/%{srcname}-%{version}-*.egg-info/

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.1-23
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.1-20
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1-17
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1-15
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1-14
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Sep 18 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.1-11
- Drop python2.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1-9
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.1-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Apr 11 2016 Jon Ciesla <limburgher@gmail.com> - 0.1-3
- Restore iconv.

* Sun Apr 10 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.1-2
- Follow packaging guidelines
- Other cleanups

* Thu Apr 07 2016 Jon Ciesla <limburgher@gmail.com> - 0.1-1
- Initial RPM release
