// CompanyList.js

import api from "./services/api";

export default function CompanyList() {
  const [companies, setCompanies] = useState([]);

  useEffect(() => {
    const fetchCompanies = async () => {
      const response = await api.get("/companies");
      setCompanies(response.data);
    };
    fetchCompanies();
  }, []);

  // return UI to display companies
}
