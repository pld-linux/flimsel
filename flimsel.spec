Summary:	flimsel is a minimalistic digitial image browser
Summary(hu.UTF-8):	flimsel egy minimalista digitális képböngésző
Name:		flimsel
Version:	0.0.6
Release:	0.1
License:	GPL v3
Group:		X11/Applications/Graphics
Source0:	http://www.ecademix.com/JohannesHofmann/%{name}-%{version}.tar.gz
# Source0-md5:	5f993c4c6ed5a5ace7cd552adf89182f
Patch0:		%{name}-epeg.patch
URL:		http://www.ecademix.com/JohannesHofmann/flimsel.html
BuildRequires:	epeg-devel
BuildRequires:	fltk-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
flimsel is a minimalistic digitial image browser based on the fltk
toolkit.

%description -l hu.UTF-8
flimsel egy minimalista digitális képbőngésző fltk alapokon.

%package example
Summary:	An example script
Summary(hu.UTF-8):	Egy példa szkript
Group:		X11/Applications/Graphics
Requires:	flimsel = %{version}-%{version}
Requires:	gimp
Requires:	libjpeg-progs

%description example
An example script that shows how to customize flimsel.

%description example -l hu.UTF-8
Egy példa-szkript, amely megmutatja, hogyan szabhatod testre a
flimsel-t.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install examples/flimsel.sh $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/flimsel.1*

%files example
%defattr(644,root,root,755)
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/%{name}.sh
