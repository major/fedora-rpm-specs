%global	gem_name		rexical

Name:		rubygem-%{gem_name}
Version:	1.0.8
Release:	3%{?dist}

Summary:	Lexical scanner generator that is used with Racc to generate Ruby programs
# LGPL-2.1-or-later: lib/rexical/generator.rb
# LGPL-2.1-only: others
License:	LGPL-2.1-only AND LGPL-2.1-or-later
URL:		https://github.com/sparklemotion/rexical
Source0:	https://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildRequires:	ruby(release)
BuildRequires:	rubygems-devel
BuildRequires:	ruby
BuildRequires:	rubygem(getoptlong)
BuildRequires:	rubygem(minitest)
BuildArch:		noarch

%description
Rexical is a lexical scanner generator that is used with Racc to generate Ruby
programs. Rexical is written in Ruby.


%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

for f in \
	DOCUMENTATION.ja.rdoc \
	README.ja \
	%{nil}
do
	iconv -f EUC-JP -t UTF-8 $f | sed -e 's|\r||' > $f.tmp
	mv $f.tmp $f
done
sed -i DOCUMENTATION.en.rdoc -e 's|\r||'

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
	%{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

rm -f %{buildroot}%{gem_cache}
pushd %{buildroot}%{gem_instdir}
rm -rf \
	Manifest.txt \
	Rakefile \
	test/ \
	%{nil}
popd

%check
pushd .%{gem_instdir}

export RUBYLIB=$(pwd):$(pwd)/lib
# Skip rubocop related test
sed -i test/test_generator.rb \
	-e 's|\(test_rubocop_security\)$|\1 ; skip "rubocop unavailable"|'

ruby -e "Dir.glob('test/**/test_*.rb'){|f| require f}"

popd

%files
%{_bindir}/rex

%dir %{gem_instdir}
%license	%{gem_instdir}/COPYING
%doc	%{gem_instdir}/README.ja
%doc	%{gem_instdir}/README.rdoc

%{gem_instdir}/bin/
%{gem_libdir}/
%{gem_spec}

%files doc
%doc	%{gem_docdir}
%doc	%{gem_instdir}/CHANGELOG.rdoc
%doc	%{gem_instdir}/DOCUMENTATION.en.rdoc
%doc	%{gem_instdir}/DOCUMENTATION.ja.rdoc
%{gem_instdir}/sample/

%changelog
* Fri Jul 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_45_Mass_Rebuild

* Tue May 26 2026 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.8-2
- Update License tag
- Prefer https over http for upstream URL

* Wed Apr 29 2026 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.8-1
- Initial package
