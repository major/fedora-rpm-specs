%{?nodejs_find_provides_and_requires}
%global npm_name nodemon

# Disable until dependencies are bundled
%global enable_tests 0

Name:          nodejs-%{npm_name}
Version:       3.1.9
Release:       %autorelease
Summary:       Simple monitor script for use during development of a node.js app
License:       ISC AND MIT
URL:           https://github.com/remy/nodemon
Source0:       %{npm_name}-v%{version}-bundled.tar.gz

BuildRequires: nodejs-devel
BuildRequires: nodejs-packaging
BuildRequires: npm

# Let the nodemon work with any nodejs version available
%global __requires_exclude ^\/usr\/bin\/node
Requires:      nodejs(engine)
Suggests:      nodejs

ExclusiveArch: %{nodejs_arches} noarch
BuildArch:     noarch

%description
Simple monitor script for use during development of a node.js app.

For use during development of a node.js based application.

nodemon will watch the files in the directory in which nodemon
was started, and if any files change, nodemon will automatically
restart your node application.

nodemon does not require any changes to your code or method of
development. nodemon simply wraps your node application and keeps
an eye on any files that have changed. Remember that nodemon is a
replacement wrapper for node, think of it as replacing the word "node"
on the command line when you run your script.

%prep
%setup -q -n %{npm_name}-%{version}

%build

# nothing to do
# tarball is bundled in --production mode, so no need to prune

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr doc bin lib package.json website node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}

mkdir -p %{buildroot}%{_bindir}
ln -sf %{nodejs_sitelib}/%{npm_name}/bin/nodemon.js %{buildroot}%{_bindir}/nodemon


#%%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
npm run test
%endif

%files
%doc CODE_OF_CONDUCT.md doc faq.md README.md
%{nodejs_sitelib}/%{npm_name}
%{_bindir}/nodemon

%changelog
%autochangelog
