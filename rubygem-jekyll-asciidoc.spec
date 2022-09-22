%global gem_name jekyll-asciidoc

Name:           rubygem-%{gem_name}
Version:        3.0.0
Release:        %autorelease
Summary:        Jekyll plugin for using AsciiDoc sources with Asciidoctor
License:        MIT

URL:            https://github.com/asciidoctor/jekyll-asciidoc
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildRequires:  ruby(release)
BuildRequires:  rubygems-devel
BuildRequires:  ruby >= 1.9.3

BuildArch:      noarch

%description
A Jekyll plugin that converts the AsciiDoc source files in your site to HTML
pages using Asciidoctor.


%package        doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}

BuildArch:      noarch

%description    doc
Documentation for %{name}.


%prep
%autosetup -n %{gem_name}-%{version} -p1


%build
gem build ../%{gem_name}-%{version}.gemspec

%gem_install


%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/


%files
%license %{gem_instdir}/LICENSE.adoc

%dir %{gem_instdir}

%{gem_libdir}

%exclude %{gem_cache}

%{gem_spec}


%files doc
%doc %{gem_docdir}

%doc %{gem_instdir}/CHANGELOG.adoc
%doc %{gem_instdir}/README.adoc
%doc %{gem_instdir}/jekyll-asciidoc.gemspec

%exclude %{gem_instdir}/.yardopts

%{gem_instdir}/Gemfile


%changelog
%autochangelog
