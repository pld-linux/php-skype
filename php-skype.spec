%define		php_min_version 5.0.0
%define		pkgname	skype
Summary:	PHP Skype API wrapper class
Name:		php-%{pkgname}
Version:	0.1.1
Release:	2
License:	PHP 3.0
Group:		Development/Languages/PHP
Source0:	http://labs.gree.jp/data/source/php-skype-%{version}.tgz
# Source0-md5:	6f154bed1f0f13a0fb729f89ed51bc6e
URL:		http://labs.gree.jp/Top/OpenSource/Skype-en.html
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.461
Requires:	php(core) >= %{php_min_version}
Requires:	php(date)
Requires:	php(dbus)
Requires:	php(pcre)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# bad depsolver
%define		_noautopear	pear
# put it together for rpmbuild
%define		_noautoreq	%{?_noautophp} %{?_noautopear}

%description
PHP Skype API wrapper class is a PHP class library to access Skype (on
Linux) via its API. With PHP DBus, this class library provides
easy-to-use interfaces to manipulate Skype on Linux.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}
cp -a Skype.php Skype $RPM_BUILD_ROOT%{php_data_dir}

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a example/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_data_dir}/Skype.php
%{php_data_dir}/Skype
%{_examplesdir}/%{name}-%{version}
