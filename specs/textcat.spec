Name:			textcat
Version:		1.10
Release:		22%{?dist}
Summary:		Written language identification
%{?el5:Group:		Applications/Text}

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:		LicenseRef-Callaway-LGPLv2+
URL:			http://www.let.rug.nl/~vannoord/TextCat/
Source0:		%{url}text_cat.tgz
Source1:		%{url}%{name}.pdf

BuildRequires:		perl-interpreter
BuildRequires:		perl-generators
BuildRequires:		perl(Benchmark)
BuildRequires:		perl(Getopt::Std)
BuildRequires:		perl(strict)
BuildRequires:		perl(vars)

BuildArch:		noarch
%{?el5:BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)}

%description
TextCat is an implementation of the text categorization algorithm
presented in Cavnar, W. B. and J. M. Trenkle, "N-Gram-Based Text
Categorization".  TextCat uses this the technique to implement a
written language identification.  At the moment, it knows about 69
natural languages (counting Esperanto as a natural language).


%prep
%setup -qc
cp -a %{SOURCE1} .


%build
sed	-e '1{/^#!.*/d}' < text_cat > %{name}
sed -i	-e '1s~^~#!%{__perl} -w\n~'						\
	-e 's!/users1/vannoord/Perl/TextCat/LM!%{_datadir}/%{name}/lm!g'	\
	%{name}
touch	-r text_cat %{name}


%install
%{?el5:rm -rf %{buildroot}}
mkdir	-p %{buildroot}%{_bindir} %{buildroot}%{_datadir}/%{name}/lm
install -pm0755 %{name} %{buildroot}%{_bindir}
install -pm0644 LM/* %{buildroot}%{_datadir}/%{name}/lm


%check
sed	-e 's!%{_datadir}/%{name}/lm!%{buildroot}&!g'				\
	< %{name} > %{name}_test
for _test in `find ShortTexts/ -name '*.txt' | sort -u`
do
  %{__perl} -w %{name}_test ${_test}
done



%files
%doc CHANGES COPYING Copyright README %{name}.pdf
%{_bindir}/%{name}
%{_datadir}/%{name}


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.10-21
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Mar 12 2014 Björn Esser <bjoern.esser@gmail.com> - 1.10-1
- initial rpm release (#1075662)
