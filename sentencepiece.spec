%define __cmake_in_source_build 1

%define _epel   %{?epel:%{epel}}%{!?epel:0}

Name:		sentencepiece
Version:	0.1.92
Release:	9%{?dist}
Summary:	An unsupervised text tokenizer for Neural Network-based text generation

License:	ASL 2.0
URL:		https://github.com/google/sentencepiece
Source0:	https://github.com/google/sentencepiece/releases/download/v%{version}/%{name}-%{version}-Source.tar.xz

BuildRequires: make
%if 0%{_epel} >= 7
BuildRequires:	cmake3
%else
BuildRequires:	cmake
%endif
BuildRequires:	gcc-c++
BuildRequires:	gperftools-devel
BuildRequires:	pkgconfig
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools

%description
The SentencePiece is an unsupervised text tokenizer for Neural Network-based
text generation.
It is an unsupervised text tokenizer and detokenizer mainly for 
Neural Network-based text generation systems where the vocabulary size is 
predetermined prior to the neural model training.
SentencePiece implements subword units and unigram language model with the 
extension of direct training from raw sentences.
SentencePiece allows us to make a purely end-to-end system that does not
depend on language-specific pre/post-processing.

%package libs
Summary:	Runtime libraries for SentencePiece

%description libs
This package contains the libraries for SentencePiece.

%package tools
Summary:	Tools for SentencePiece
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}

%description tools
This package contains tools for manipulate models for SentencePiece.

%package devel
Summary:	Libraries and header files for SentencePiece
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}

%description devel
This package contains header files to develop a software using SentencePiece.

%package        -n python3-%{name}
Summary:	Python module for SentencePiece
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
%{?python_provide:%python_provide python3-%{name}}

%description -n python3-%{name}
This package contains Python3 module file for SentencePiece.

%prep
%autosetup -n %{name}-%{version}-Source

%build
%if %{_epel} >= 7
cmake3 . -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCMAKE_INSTALL_LIBDIR=%{_libdir}
%else
%cmake . -DCMAKE_INSTALL_LIBDIR=%{_libdir}
%endif
%make_build
pushd python
CFLAGS="-I../src" LDFLAGS="-L../src -lsentencepiece" PKG_CONFIG_PATH=".." %{__python3} setup.py build
popd

%install
%make_install
pushd python
PKG_CONFIG_PATH=".." %py3_install
popd
sed -i'' -e "s,%{buildroot},," %{buildroot}%{_libdir}/pkgconfig/sentencepiece.pc
sed -i'' -e "s,${prefix}/lib,%{_libdir}," %{buildroot}%{_libdir}/pkgconfig/sentencepiece.pc
find %{buildroot} -name '*.a' -delete

%files libs
%doc README.md
%license LICENSE
%{_libdir}/libsentencepiece*.so.0*

%files devel
%{_includedir}/sentencepiece*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/sentencepiece*.pc

%files tools
%{_bindir}/spm*

%files -n python3-%{name}
%{python3_sitearch}/%{name}.py
%{python3_sitearch}/_%{name}*.so
%{python3_sitearch}/__pycache__/*
%{python3_sitearch}/%{name}-*.egg-info/


%changelog
* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.92-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.92-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.1.92-7
- Rebuilt for Python 3.11

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.92-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.92-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.1.92-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.92-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Oct 07 2020 Kentaro Hayashi <kenhys@gmail.com> - 0.1.92-2
- Add missing BuildRequires: python3-setuptools

* Thu Oct 01 2020 Kentaro Hayashi <kenhys@gmail.com> - 0.1.92-1
- New upstream release

* Tue Sep 22 2020 Jeff Law <law@redhat.com> - 0.1.84-6
- Use cmake_in_source_build to fix FTBFS due to recent cmake macro changes

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.84-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.84-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.84-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.84-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 14 2019 Kentaro Hayashi <hayashi@clear-code.com> - 0.1.84-1
- New upstream release

* Mon Oct 07 2019 Kentaro Hayashi <hayashi@clear-code.com> - 0.1.83-1
- initial packaging
